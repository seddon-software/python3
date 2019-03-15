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
columns = 2
figA, (ax11, ax12) = plt.subplots(row, columns, sharey=True)
figB, (ax21, ax22) = plt.subplots(row, columns, sharey=True)
ax11.plot(t, t,    redDashes)
ax12.plot(t, t**2, blueSquares)  
ax21.plot(t, t**3, greenTriangles)
ax22.plot(t, t,    redDashes)
ax12.set_title("axis 11")
ax12.set_title("axis 12")
ax21.set_title("axis 21")
ax22.set_title("axis 22")
figA.canvas.set_window_title('Figure A')
figB.canvas.set_window_title('Figure B')
 
plt.show()
pyplot.close()

