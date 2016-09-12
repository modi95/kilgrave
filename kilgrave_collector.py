import multiprocessing
import socket
import struct
import time

from config import *

collector_server = None

class kilgrave_collector():

  # Initializes an object of type #kilgrave_collector
  # Values for initialization are in config.py
  def __init__(self):
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # self.server_socket.settimeout(len(target_machines)*3)
    self.server_socket.settimeout(5)
    # self.server_socket.setblocking(True)
    self.server_socket.bind((socket.gethostname(), collector_port))
    self.server_socket.listen(len(target_machines))
    self.output_file = open('output_file', 'w')

  def wait_for_response(self):
    print('Kilgrave collector waiting for response on')
    print('host:{} port:{}'.format(socket.gethostname(), collector_port))
    connection, executor_address = self.server_socket.accept()
    print('Kilgrave accepting response from {}'.format(executor_address))
    self.write_response(connection, executor_address)

  def write_response(self, connection, executor_address):
    self.output_file.write('\r\nKilgave Executor {} Response \r\n'.format(executor_address))
    output_length = connection.recv(arg_length_size)
    order_output = connection.recv(int(output_length))
    print('Received {} lines'
      .format(len(order_output.split('\n'))))
    self.output_file.write(order_output + '\r\n\r\n END OF RESPONSE \r\n')

  def shutdown(self):
    self.output_file.close()
    self.server_socket.close()

def main():
  global collector_server
  collector_server = kilgrave_collector()
  try:
    for i in range(len(target_machines)):
      #try:
      collector_server.wait_for_response()
      #except socket.error as ex:
      #  if str(ex) == "[Errno 35] Resource temporarily unavailable":
      #    time.sleep(1)
      #    print('Errno 35 Happened')
      #    continue
    collector_server.shutdown()
  except KeyboardInterrupt:
    print("Shutting Down Kilgrave Collector")
    collector_server.shutdown()
  except socket.timeout:
    print("Done waiting, some machines appear to have died :(")

if __name__ == "__main__":
  main()
