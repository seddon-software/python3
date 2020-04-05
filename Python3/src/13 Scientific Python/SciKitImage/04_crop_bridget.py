import os, sys
from PIL import Image


os.chdir("images")
infile = "bridget.jpg"

outfile = os.path.splitext(infile)[0] + ".cropped.jpg"
try:
    img = Image.open(infile)
    print(img.size)
    left = 500
    upper = 0
    right = 1100
    lower = 800
    box = (left, upper, right, lower)
    img = img.crop(box)
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
