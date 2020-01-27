import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import log, sqrt
import PIL
from scipy.optimize import curve_fit

def load_image(fileName):
    image = PIL.Image.open(fileName)
    image.load()
    return np.asarray(image, dtype="float")

def gauss2D(xy_tuple, peak, μ, σ):
    # e-(x²+y²)/2σ²/2πσ²
    x, y = xy_tuple
    z = peak*np.exp(-(x-μ)**2-(y-μ)**2/(2.*σ**2))
    return np.ravel(z)

def main():
    fileName = "data/gaussian.tif"
    image = load_image(fileName)
    data = image[()]
    print(data)
    
    plt.gcf().canvas.set_window_title(fileName)
    plt.gca().set_title("2D Gaussian fitting")
    
    def initialGuess():    
        peak = 0.04
        center = -1.3
        FWHM = fullWidthAtHalfMaximum = 0.1
        k = 2 * sqrt(2 * log(2))
        standard_deviation = FWHM / k
        return [peak, center, standard_deviation]
    fit, estimated_covariance = curve_fit(gauss, x, dy, p0=initialGuess())
    print(fit)
    plt.plot(x, dy)
    plt.plot(x, gauss(x, *fit), 'r-',
             label=f'peak={fit[0]:.2f} μ={fit[1]:.2f} σ={fit[2]:.2f}')
    plt.legend()
    plt.show()


main()

