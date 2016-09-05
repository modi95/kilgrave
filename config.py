target_machines_prod = [
  'fa16-cs425-g22-01.cs.illinois.edu',
  'fa16-cs425-g22-02.cs.illinois.edu',
  'fa16-cs425-g22-03.cs.illinois.edu',
  'fa16-cs425-g22-04.cs.illinois.edu',
  'fa16-cs425-g22-05.cs.illinois.edu',
  'fa16-cs425-g22-06.cs.illinois.edu',
  'fa16-cs425-g22-07.cs.illinois.edu',
  'fa16-cs425-g22-08.cs.illinois.edu',
  'fa16-cs425-g22-09.cs.illinois.edu',
  'fa16-cs425-g22-10.cs.illinois.edu'
]

target_machines = [
  '10.192.193.212',
]

executor_port = 27508
disseminator_port = 27509
collector_port = 27510

execution_ack_string = "ack\r\n"

# This is the number of characters that represent the length of the command.
arg_length_size = 4 

# Creates a string of predefined size containing the length of the command
# that the 
def length_padder(length):
  length = str(length)
  length_string = '0'*(arg_length_size-len(length)) + length
  return length_string
