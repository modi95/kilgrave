from config import *
import struct
import socket

class kilgrave_executor():

  # Initializes an object of type #kilgrave_executor
  # Values for initialization are in config.py
  def __init__():
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((socket.gethostname(), executor_port))
    server_socket.listen(5) # We don't expect this to receive many requests

  # Waits for an execution order from a kilgrave_disseminator
  # Once this order is received, it returns the order string.
  def wait_for_order():
    connection, address = server_socket.accept()
    print ("Kilgrave Initiated from {}".format(client_address))
    data = connection.recv(arg_length_size)
    order = connection.recv(int(data))
    retrun order

if __name__ == "__main__":
  executor_server = kilgrave_executor()
  order = executor_server.wait_for_order()
  print order

