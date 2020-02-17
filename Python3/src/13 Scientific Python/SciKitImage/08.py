import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import skimage.measure as measure
import skimage.morphology as morphology
import scipy.ndimage as nd
from skimage import io as skio
import skimage.io as skio


infile = "images/smart_lady.jpeg"
img = Image.open(infile)
width, height = img.size
print(width, height)
image = np.asarray( img, dtype="int32" )
filter01 = (image[:,:,0] > image[:,:,1])
filter02 = (image[:,:,0] > image[:,:,2])
filter12 = (image[:,:,1] > image[:,:,2])

c1 = [127, 127, 127]
c2 = [255,   0, 255]
c3 = [255, 255,   0]
c4 = [  0, 180,   0]
c5 = [ 10,  20,  30]
c6 = [  0,  80,  80]

# image[~filter01] = c1
# image[~filter02] = c2
# image[~filter12] = c3
image[ filter01] = c1
image[ filter02] = c6
image[ filter12] = c5
plt.imshow(image)
plt.show()

