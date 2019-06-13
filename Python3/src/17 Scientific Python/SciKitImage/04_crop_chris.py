import os, sys
from PIL import Image


os.chdir("images")
infile = "chris.JPG"

outfile = os.path.splitext(infile)[0] + ".cropped.jpg"
try:
    img = Image.open(infile)
    box = (2200, 930, 2650, 1600)
    img = img.crop(box)
    img.show()
    img.save(outfile, "JPEG")
except IOError as e:
    print(e)
