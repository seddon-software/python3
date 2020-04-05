import os, sys
from PIL import Image


os.chdir("images")
infile = "joshua.jpg"

outfile = os.path.splitext(infile)[0] + ".cropped.jpg"
try:
    img = Image.open(infile)
    img = img.rotate(-90)
    left = 1100
    upper = 300
    right = 2100
    lower = 1800
    box = (left, upper, right, lower)
    img = img.crop(box)
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
