import scisoftpy as dnp
from math import sin, cos

X = dnp.arange(0, 10)
Y = dnp.arange(0, 10)
print X, X.shape
print Y, Y.shape

Z = [sin(x)*cos(y) for x in X for y in Y]
Z = dnp.asarray(Z)
Z = Z.reshape(10,10)
dnp.plot.setdefname('Surface Plot')
dnp.plot.surface(Z)
