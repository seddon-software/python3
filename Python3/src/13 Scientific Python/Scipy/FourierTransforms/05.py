import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy import sin, pi as π
import scipy.integrate as integrate

def stairFunction(t):
    x = t % 6
    if x > 5: return 5
    if x > 4: return 4
    if x > 3: return 3
    if x > 2: return 2
    if x > 1: return 1
    return 0

stairFunction = np.vectorize(stairFunction)


t = np.arange(0, 20, 0.1)
y = stairFunction(t)
result = integrate.quad(stairFunction, 0, 10)
print(result)
plt.plot(t, y)
plt.show()

