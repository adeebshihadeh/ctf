a = "99 40 80 4E 82 D3 74 E5 12 E8 31 _ 9E D6 D2 2B D5 D1 _ C8 17 1E 83 F4 20 _ 13 14 68 05 86 30 89 A1 16 C4 8E FF DA 1E 0D 14 58 _ D2 ED 5E 2D BE 89 3B 63 2D 46 72 1C _ 8D 82 _ EB D0 DC 72 69 B9 12 B6"

a = "ec f3 2b 03 7f 4b f8 05 75 6f 45 30 14"

a = a.replace(" _", "")
a = a.lower().split(" ")
# a = "".join(map(chr, a))


s = ""
for i in a:
  # s += chr(int("0x" + i))
  s += chr(int("0x" + i, 16))
print s
