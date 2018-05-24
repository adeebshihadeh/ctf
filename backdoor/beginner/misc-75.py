import requests

url = "http://hack.bckdr.in/2013-MISC-75/misc75.php"

p = open("primes.txt").read().split(" ")

session = requests.session()

r = requests.get(url)

n = int(r.text.split("First ")[1].split(" prime")[0])

n = 10

sum = 0
for i in range(0, n):
 sum += int(p[i])

r = requests.post(url, data={'answer': sum})

print r.status_code
print r.text
