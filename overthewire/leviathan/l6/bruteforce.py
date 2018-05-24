from subprocess import call, STDOUT

for i in range(10):
	for x in range(10):
		for a in range(10):
			for l in range(10):
				print str(i) + str(x) + str(a) + str(l)
				if 6 != call(["./leviathan6", str(i) + str(x) + str(a) + str(l)], stderr=STDOUT):
					break
