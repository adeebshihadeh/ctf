from subprocess import check_output


cities = open("cities.txt").read().split("\n")

d = "/Volumes/CDROM"

for c in cities:
  try:
    a = check_output(["grep", "-ir", '"' + c.lower() + '"' , d])
    print a, c.lower()
  except:
    pass

