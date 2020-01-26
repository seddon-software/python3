import scisoftpy as dnp
from math import sin, cos

# numpy broadcasting not working in this version of scipy
# this code is a workaround
x = dnp.arange(0, 10, 0.1)
y = dnp.arange(0, 10, 0.1)
n = x.shape[0]
print "Shape of x:", n

z = dnp.zeros(n*n).reshape(n,n)
for i in range(n):
    for j in range(n):
        a = x[i]
        b = y[j]
        z[i][j] = a * a * sin(b) + b * b * cos(a)
#         z[i][j] = x[i]*x[i]*math.sin(x[i]) + y[j]*y[j]*math.sin(y[i]) 

dnp.plot.setdefname('Plot 1')
dnp.plot.image(z)
 
dnp.plot.setdefname('Plot 2')
dnp.plot.surface(z)
print "done"

