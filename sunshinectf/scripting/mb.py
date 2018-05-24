import socket
import re
import os
import sys
from time import sleep

def parse(a):
  d = {}
  for l in a.split("\n"):
    if "DIR" in l or "FILE" in l:
      l = re.sub(' +', ' ', l).rstrip().split(' ')
      d[l[0]] = {"name": l[0], "type": l[1], "size": l[2]}
  return d

def fastrecv(sock):
  msg = sock.recv(2048)
  while ": $ " not in msg.split("\n")[-1]:
    msg += sock.recv(2048)
  num = msg.split(": (")[1].split(" entries)")[0]
  # if int(num) != len(msg.split("\n")[1:-1]):
  #   print "="*10, "error n", num, "len", len(msg.split("\n")[1:-1]), "="*10
  #   sleep(0.2)
  #   msg += sock.recv(2048)
  return msg 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('chal1.sunshinectf.org', 30001))
s.recv(2048)
s.send("start\n")
s.recv(2048)


def explore(dir):
  print "dir", dir
  s.send("cd " + dir + "\n")
  s.recv(1024)
  s.send("ls\n")
  d = parse(fastrecv(s))

  sum_ = 0
  for f in d:
    if d[f]["type"] == "DIR":
      explore(os.path.join(dir, f))
    sum_ += int(d[f]["size"])
  
  s.send("cd ..\n")
  s.recv(1024)
  s.send("ls\n")
  t = parse(fastrecv(s))[dir.split("/").pop()]["size"]
  if int(t) != sum_:
    print "="*8, "sending", "="*8
    print "t", t, "sum", sum_, "corrupt", int(t) != sum_
    print "diff", int(t) - sum_
    s.send("send " + dir + "\n")
    sleep(0.1)
    res = s.recv(2048)
    if "Hooray!" in res:
      print "="*20, "HOORAY", "="*20
      print res
      raise Exception("end")


for _ in range(0, 20):
  try:
    explore("/")
  except:
    print "="*10, _+1, "complete", "="*10

print "it's over"