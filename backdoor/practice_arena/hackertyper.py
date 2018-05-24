import urllib2

a = "http://hack.bckdr.in/HACKER-TYPER/console/cca6d59f9bb7ac09455360c0c3647e34.txt"

for line in urllib2.urlopen(a).read().split("\n"):
  if len(line) == 32:
    print urllib2.urlopen("http://hack.bckdr.in/HACKER-TYPER/console/" + line + ".txt").read()
