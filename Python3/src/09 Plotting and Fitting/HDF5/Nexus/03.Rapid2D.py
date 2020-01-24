# Dawn/Data Browsing
#    i22-4996.nxs
#    MoKedge_1_15.nxs
# ... Meta Header Table:    this shows keys/values
# ... Data Analysis/Data:    this shows data sets

import h5py
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import savgol_filter

# open Nexus file
f = h5py.File("i22-4996.nxs", "r")

# get dataset
ds = f["/entry1/Rapid2D"]

# convert to numpy array
data = ds["data"][()]

# check shape (1,1,512,512)
print(data.shape)

# extract data as 2D array
image = data[0,0]

# fig, (ax1, ax2) = plt.subplots(2, 1)
# 
# ax1.imshow(image)
Z = image[260:280, 195:230]
#Z = image[:, :]
print(Z.shape)
X = np.arange(Z.shape[1])
Y = np.arange(Z.shape[0])
X, Y = np.meshgrid(X, Y) 
print(X.shape)
print(Y.shape)

#ax2.imshow(subImage)

fig = plt.figure()
ax2 = fig.gca(projection='3d')
surf = ax2.plot_surface(X, Y, Z, cmap='terrain')

plt.show()

