import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter  # for smoothing

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

def setupAxes(yLabel):
    set_title("MoKedge_1_15.nxs")
    ax = plt.gca()
    ax.set_facecolor((1.0, 0.9, 0.6))
    ax.set_xlabel('X')
    ax.set_ylabel(yLabel)
    ax.xaxis.set_label_position("top")
    ax.yaxis.set_label_position("right")
    plt.grid(True)

fileName = "data/MoKedge_1_15.nxs"
f = h5py.File(fileName, "r")

Y = f["/entry1/counterTimer01/It"][()]
X = np.arange(len(Y))
Ŷ = savgol_filter(Y, 25, 3) # smoothing window size 25, polynomial order 3
dY = np.diff(Y)
dŶ = savgol_filter(dY, 25, 3) # smoothing window size 25, polynomial order 3

k̂wargs = {'linewidth':3, 'color':'blue'}
kwargs = {'linewidth':1, 'color':'red'}

# plot It
setupAxes('It')
plt.plot(X, Ŷ, **k̂wargs)
plt.plot(X, Y, **kwargs)
plt.show()

# plot d(It)
setupAxes('d(It)')
left = 280
right = 70
plt.plot(X[left:-right-1], dŶ[left:-right], **k̂wargs)
plt.plot(X[left:-right-1], dY[left:-right], **kwargs)
plt.show()

