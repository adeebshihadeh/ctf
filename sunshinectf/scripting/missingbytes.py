import socket
import re
from time import sleep

def parse(a):
  d = {}
  for l in a.split("\n"):
    if "DIR" in l or "FILE" in l:
      l = re.sub(' +', ' ', l).rstrip().split(' ')
      d[l[0]] = {"name": l[0], "type": l[1], "size": l[2]}
  return d

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('chal1.sunshinectf.org', 30001))

print s.recv(2048)

s.send("start\n")
print s.recv(2048)

fs = {}

def explore(dir):
  s.send("cd " + dir + "\n")
  sleep(0.1)
  s.recv(1024)
  s.send("ls\n")
  sleep(0.2)
  fs[dir] = parse(s.recv(2048))
  files = True
  sum = 0
  for f in fs[dir]:
    if fs[dir][f]["type"] == "DIR":
      files = False
      print "dir:", f
      explore(dir + "/" + f)
    sum += int(fs[dir][f]["size"])

  if files:
    s.send("cd ..\n")
    s.recv(1024)
    s.send("ls\n")
    sleep(0.2)
    d = parse(s.recv(2048))
    if d[dir][size] != sum:
      s.send("send " + dir + "\n")
      sleep(0.2)
      print "="*4, s.recv(2048), "="*4

  print fs

explore("/")
