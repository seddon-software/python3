'''
masked arrays
'''

import numpy as np
import numpy.ma as ma

a = np.random.randint(low=0, high=100, size=(100)); print(a)
z = a<50
print(z)
mask = ma.masked_array(a, mask=a<=50)

print(a)
print(mask)
print(mask.mean())
