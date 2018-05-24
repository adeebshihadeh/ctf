import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ctf.hackucf.org', 10101))

while True:
  a = 0
  m = s.recv(2048)
  while "Repeat:" not in m:
    m += s.recv(2048)
    a += 1
    if a > 4:
      print m
      break
  n = m.split("Value: ")[1].split("\nRepeat")[0]
  print m
  print n
  s.send(n + "\n")

