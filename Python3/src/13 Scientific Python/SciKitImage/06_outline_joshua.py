import os, sys
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import skimage.morphology as morphology
import skimage.feature as feature
from PIL import Image
import time


def doit(image, sigma, threshold, spread, dt):
    low = threshold / 256.0
    high = (threshold + spread) / 256.0
    set_title(f"sigma={sigma} low={low*256} high={high*256}")
    edges = feature.canny(image, sigma=sigma, low_threshold=low, high_threshold=high)
    plt.imshow(edges, cmap=plt.cm.gray) #    plt.show()
    plt.draw()
    plt.pause(0.001)
    time.sleep(dt)

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

def load_image(infilename):
    img = Image.open(infilename)
    img.load()
    data = np.asarray( img, dtype="int32" )
    return data

plt.ion()
image = load_image("images/joshua.cropped.jpg")
image = image / 256.0
image = image[:,:,0]

for sigma in range(1, 2):
    for threshold in range(31, 32):
        for spread in range(2, 3):
            doit(image, sigma, threshold, spread, dt=5.0)
