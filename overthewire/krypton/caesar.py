a = "OMQEMDUEQMEK"

for i in range(1, 26):
  plain = ""
  for c in a:
    char = chr(ord(c) + i)
    char = char if ord(char) <= ord('Z') else chr(ord(char)-26)
    plain += " " if c == " " else char
  print plain
