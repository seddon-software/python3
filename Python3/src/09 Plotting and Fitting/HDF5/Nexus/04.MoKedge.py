# Nexus files can be viewed in Dawn
#
# In Dawn use the Data Browsing prospective.
# Use the "Meta Header Table" window to show key/value pairs from the Nexus/HDF5 file
# Use the "Data Analysis/Data" window to view datasets

import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter  # for smoothing

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

fileName = "MoKedge_1_15.nxs"
f = h5py.File(fileName, "r")

Y = f["/entry1/counterTimer01/It"][()]
X = np.arange(len(Y))
Ŷ = savgol_filter(Y, 25, 3) # smoothing window size 25, polynomial order 3

ax = plt.gca()
ax.set_facecolor((0.3, 0.5, 0.3))
ax.set_xlabel('X')
ax.set_ylabel('counterTimer01/It')
ax.xaxis.set_label_position("top")
ax.yaxis.set_label_position("right")
plt.plot(X, Ŷ, linewidth=3, color="white")
plt.plot(X, Y)
plt.grid(True)
set_title("/entry1/counterTimer01/It")
plt.show()
