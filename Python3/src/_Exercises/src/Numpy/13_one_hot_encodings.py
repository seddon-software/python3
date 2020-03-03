def one_hot_encodings(arr):
    unique = np.unique(arr)
    out = np.zeros((arr.shape[0], unique.shape[0]))
    for i, k in enumerate(arr):
        out[i, list(unique).index(k)] = 1
    return out

import numpy as np
a = np.random.randint(low=10, high=15, size=(30,)); print(a)
hot = one_hot_encodings(a)
print(hot)
