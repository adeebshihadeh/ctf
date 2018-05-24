import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('ctf.hackucf.org', 10104))

while True:
  a = 0
  m = s.recv(2048)
  while " =" not in m:
    m += s.recv(2048)
    a += 1
    if a > 4:
      print m
      break
  m = m.split("\n")[-1]
  n = m.split(" =")[0]
  print m
  print n
  s.send(str(eval(n)) + "\n")

