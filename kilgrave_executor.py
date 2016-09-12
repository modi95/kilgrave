import struct
import socket
import time
from subprocess import check_output
import os # TODO (@akmodi): Change this to subprocess

from config import *

# This variable will keep an instance of kilgrave_executor. It's being created
# as a global variable so that the server can be properly shut down in case of
# a keyboard interrupt.
executor_server = None

class kilgrave_executor():

  # Initializes an object of type #kilgrave_executor
  # Values for initialization are in config.py
  def __init__(self):
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_socket.bind((socket.gethostname(), executor_port))
    self.server_socket.listen(5) # We don't expect this to receive many requests

  # Waits for an execution order from a kilgrave_disseminator
  # Once this order is received, it returns the order string.
  def wait_for_order(self):
    print("Kilgrave executor waiting for order on")
    print("host:{} port:{}".format(socket.gethostname(), executor_port))
    connection, disseminator_address = self.server_socket.accept()
    print("Kilgrave Initiated from {}".format(disseminator_address))
    data = connection.recv(arg_length_size)
    order = connection.recv(int(data))
    connection.send(execution_ack_string)
    return((order, disseminator_address))

  def check_special_order(self, order):
    if order in special_orders.keys():
      special_orders[order](self.server_socket)
      return True
    return False

  def execute_order(self, order):
    # TODO(@akmodi): Change this to subprocess.
    order_output = os.popen(order).read()
    return order_output

  def shutdown(self):
    self.server_socket.close()

  def report_output(self, order_output, listener_address):
    attempts = 3 # TODO(akmodi): set this in a better way
    while (attempts > 0):
      try:
        attempts -= 1
        time.sleep(1)
        print(order_output)
        collector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        collector.connect((listener_address[0], collector_port))
        order_response = length_padder(len(order_output)) + order_output
        collector.sendall(order_response)
        collector.close()
        print('report sent')
      except socket.error as er:
        if er.errno == errno.ECONNREFUSED:
          print("Collector connection refused. Trying again")
          continue
        else:
          raise er
    print("Giving up. Report not sent")

def main():
  global executor_server
  executor_server = kilgrave_executor()
  while (True):
    order, listener_address = executor_server.wait_for_order()
    print(order)
    if executor_server.check_special_order(order):
      continue
    order_output = executor_server.execute_order(order)
    executor_server.report_output(order_output, listener_address)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    # Space at the start of string because ^C
    print(" Shutting Down Kilgrave Executor")
    executor_server.shutdown()

