'''
Extract numbers divisible by 3 from a 2D numpy array and produce a 1D array
'''
import numpy as np

a = np.arange(10, 40).reshape(3, 10)

b = a[a % 3 == 0]
print(f"a = {a}")
print(f"b = {b}")

 