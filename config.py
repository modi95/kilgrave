
# List containing the hostnames of all the machines in your system.
target_machines = [
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

# These port numbers were chosen arbitrarily. Feel free to change them.
#target_machines = [
#  'Modi-MBP13-md.local',
#]

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

def kill(executor_socket):
  executor_socket.close()
  exit()

def update(executor_socket):
  executor_socket.close()
  import os
  os.system('exec ~/kilgrave/scripts/update.sh')
  exit()

def restart(executor_socket):
  executor_socket.close()
  import os
  os.system('exec ~/kilgrave/scripts/restart.sh')
  exit()

def nop(executor_socket):
  return

special_orders = {
  '-kill':kill,         # kill the kilgrave process
  '-update':update,     # update the kilgrave version
  '-restart':restart,   # restart kilgrave
  '-nop':nop            # do nothing; just return ack
}


