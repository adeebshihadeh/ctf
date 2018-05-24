

t = open("secret_message.txt").read()
t = t.lower()

sub = {
  'f': 'a',

  'h': 'e'
}


plain = ""
for c in t:
  if c.isalpha():
    plain += '_' if c not in sub else sub[c]
  else:
    plain += c

print plain