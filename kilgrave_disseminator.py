import struct
import socket
import sys

from config import *

def send_orders(order):
  for machine in target_machines:
    executor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    executor.connect((machine, executor_port))
    executor.sendall(order)
    response = executor.recv(len(execution_ack_string))
    print (response)
    executor.close()

def build_order():
  raw_order = ' '.join(sys.argv[1:])
  kilgrave_order = length_padder(len(raw_order)) + raw_order
  print(kilgrave_order)
  return kilgrave_order

if __name__ == "__main__":
  if (len(sys.argv) == 1):
    print("You can't run kilgrave without args")
    exit(1)
  order = build_order()
  send_orders(order)

