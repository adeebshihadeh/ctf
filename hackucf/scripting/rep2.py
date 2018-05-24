import socket
import sys
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ctf.hackucf.org', 10102))

sleep(0.2)

vals = []

repeat = True

while True:
  m = s.recv(2048)
  while "Repeat:" not in m:
    m += s.recv(2048)
    if "First:" in m:
      print m
      repeat = False
      break
  if not repeat:
    break
  n = m.split("Value: ")[1].split("\nRepeat")[0]
  print m
  print n
  vals.append(n)
  s.send(n + "\n")

s.send(vals[0] + "\n")
sleep(0.1)
print s.recv(2048)



