import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

k = 10.0
m = 1.0

class Particle:
    def __init__(self, name, x, v):
        self.name = name
        self.x = x
        self.v = v
    def getPosition(self):
        return self.x
    def next(self, dt):
        x = self.x[0]
        y = self.x[1]
        z = self.x[2]
        R = (x**2 + y**2 + z**2)**0.5
        Rhat = np.array([x, y, z])/R
        F = -k * Rhat / R**2
        # F = m * dv/dt
        dv = F * dt / m
        self.v += dv
        # dx/dt = v
        self.x += self.v * dt
         
p = Particle("earth", np.array([90.0, 0.0, 0.0]), np.array([0.0,0.2,0.1]))

X = []
Y = []
Z = []
for _ in range(60000):
    x, y, z = p.getPosition()
    X.append(x)
    Y.append(y)
    Z.append(z)
    p.next(0.1)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(X, Y, Z)
ax.scatter([0], [0], [0], s=100.0, c='red', marker='o')

plt.show()


        