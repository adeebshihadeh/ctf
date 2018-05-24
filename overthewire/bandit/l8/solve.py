lines = open("data.txt").readlines()
occurences = dict((i, lines.count(i)) for i in set(lines))

for line in occurences:
  if occurences[line] == 1:
    print line