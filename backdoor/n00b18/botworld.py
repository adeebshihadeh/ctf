import requests
import os
from subprocess import check_output, call
from PIL import Image
from io import BytesIO

url = "http://hack.bckdr.in/BOT-WORLD/"

session = requests.session()

r = requests.get(url)

for i in range(0, 101):
  img = r.text.split("img src='")[1].split("'><br>")[0]
  r = requests.get(url + img)
  image = Image.open(BytesIO(r.content)).convert('RGB')
  image.save("tmp.png")

  # os.system("convert tmp.png -colorspace Gray tmp.png")
  call(["convert", "tmp.png", "-colorspace", "Gray", "-contrast", "-flatten", "tmp.png", ">", "/dev/null"])
  t = check_output(["tesseract", "-psm", "7", "tmp.png", "-"])
  print "tess: ", t

  r = requests.post(url, data={'captcha': t})
  os.remove("tmp.png")

  if i > 90 or r.status_code != 200:
    print "="*4, i, "="*4
    print r.status_code
    print r.text


