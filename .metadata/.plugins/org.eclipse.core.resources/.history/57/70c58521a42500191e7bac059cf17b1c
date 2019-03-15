############################################################
#
#    multiple plots
#
############################################################

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(0.0, 5.0, 0.200)
redDashes = "r--"
blueSquares = "bs"
greenTriangles = "g^"

row = 1
columns = 3
fig, (ax1, ax2, ax3) = plt.subplots(row, columns, sharey=True)
ax1.plot(t, t,    redDashes)
ax2.plot(t, t**2, blueSquares)  
ax3.plot(t, t**3, greenTriangles)
ax1.set_title("axis 1")
ax2.set_title("axis 2")
ax3.set_title("axis 3")
plt.gcf().canvas.set_window_title('Figure')
 
plt.show()

