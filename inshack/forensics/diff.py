from os import listdir
from subprocess import check_output

dir = "42/4/"
hash = "f1bfedec57db740c9611a4acc9961d41"

a = listdir(dir)

for f in a:
  if check_output(["md5", "-q", dir + f]).strip() != hash:
    print check_output(["md5", "-q", dir + f])

