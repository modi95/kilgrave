
# List containing the hostnames of all the machines in your system.
target_machines = [
]

# These port numbers were chosen arbitrarily. Feel free to change them.
executor_port = 27508
disseminator_port = 27509
collector_port = 27510

execution_ack_string = "ack\r\n"

# This is the number of characters that represent the length of the command.
arg_length_size = 4 

# Creates a string of predefined size containing the length of socket message.
def length_padder(length):
  length = str(length)
  length_string = '0'*(arg_length_size-len(length)) + length
  return length_string

