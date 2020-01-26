import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_csv("../data/14763.dat", 
                    skiprows = 6,
                    engine = 'python',
                    sep = '[ \t]+')

print(data)
print(data.keys())

# dnp.plot.setdefname('Raw Data Plot')
# x = data['gonx'][100:-201]
# y = data['i_pin'][100:-200]
x = data['gonx'][250:-401]
y = data['i_pin'][250:-400]
dy = np.diff(y)

def gauss(x, peak, mu, sigma):
    return peak*np.exp(-(x-mu)**2/(2.*sigma**2))

peak = 0.04
center = -1.3
FWHM = fullWidthAtHalfMaximum = 0.1
standard_deviation = FWHM / 2.355 
from math import log, sqrt
k = 2 * sqrt(2 * log(2))
standard_deviation = FWHM / k
initial_guess = [peak, center, standard_deviation]
fitted_parameters, estimated_covariance = curve_fit(gauss, x, dy, p0=initial_guess)
print(fitted_parameters)
plt.plot(x, dy)
plt.plot(x, gauss(x, *fitted_parameters), 'r-')
plt.show()



