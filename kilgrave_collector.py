import struct
import socket

from config import *

collector_server = None

class kilgrave_collector():

  # Initializes an object of type #kilgrave_collector
  # Values for initialization are in config.py
  def __init__(self):
    self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_socket.bind((socket.gethostname(), collector_port))
    self.server_socket.listen(len(target_machines_prod))
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
    self.output_file.write(order_output + '\r\n\r\n END OF RESPONSE \r\n')

  def shutdown(self):
    self.output_file.close()
    self.server_socket.close()

def main():
  global collector_server
  collector_server = kilgrave_collector()
  for i in range(len(target_machines)):
    collector_server.wait_for_response()


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print (' Shutting Killgrave Collector')
    collector_server.shutdown()
