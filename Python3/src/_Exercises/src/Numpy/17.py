import numpy as np

np.random.seed(10)
a = np.random.randint(20, size=10)
print(a)

print(a.argsort().argsort())
print('Array: ', a)
