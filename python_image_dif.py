from PIL import ImageChops, Image
import requests

url = 'https://www.google.lk/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
fileName = 'google.png'
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()

im1 = Image.open("google.png")
im2 = Image.open("C:\\Users\\kushanlk\\desktop\\google.png")
try:
    diff = ImageChops.difference(im2, im1)

except ValueError:
   print("Images are different....")