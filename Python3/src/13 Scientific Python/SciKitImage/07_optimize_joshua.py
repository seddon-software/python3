import os, sys
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import skimage.morphology as morphology
import skimage.feature as feature
from PIL import Image
import time
import scipy.misc
from matplotlib.colors import ListedColormap

def createColorMap():
    N = 2
    vals = np.ones((N, 4))
    # colormap goes from nearly white to white
    vals[:, 0] = np.linspace(0.8, 1, N)
    vals[:, 1] = np.linspace(0.8, 1, N)
    vals[:, 2] = np.linspace(0.8, 1, N)
    print(vals)
    return ListedColormap(vals)

def doit(image, sigma, threshold, spread, dt):
    low = threshold / 256.0
    high = (threshold + spread) / 256.0
    set_title(f"sigma={sigma} low={low*256} high={high*256}")
    edges = feature.canny(image, sigma=sigma, low_threshold=low, high_threshold=high)
    edges = np.invert(edges)
    plt.imshow(edges, cmap=createColorMap())
    plt.draw()
    plt.axis('off')
    plt.savefig("outfile.pdf")
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
#figsize=(16.53, 11.69)
sigma = 0
threshold = 32
spread = 2
doit(image, sigma, threshold, spread, dt=5)
