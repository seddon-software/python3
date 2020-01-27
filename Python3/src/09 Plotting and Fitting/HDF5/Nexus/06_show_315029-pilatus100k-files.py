import os
import numpy as np
import matplotlib.pyplot as plt
import PIL
import time


def doit(fileName):
    set_title(f"title")
    data = load_image(fileName)
    plt.imshow(data, cmap=plt.cm.gray)
    plt.draw()
    plt.pause(0.001)
    time.sleep(0.1)

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

def load_image(infilename):
    img = PIL.Image.open(infilename)
    img.load()
    data = np.asarray( img, dtype="float" )
    return data

plt.ion()

os.chdir("315029-pilatus100k-files")

for n in range(1, 42):
    tif = f"{n:05}.tif"
    doit(tif)

