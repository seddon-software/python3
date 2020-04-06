import numpy as np
import PIL.Image
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.feature import canny

plt.subplots(dpi=72*2)

tablets = io.imread("images/tablets.jpg", as_gray=True)
# print(tablets)


image = PIL.Image.open("images/tablets.jpg")
image.load()
#image = image.convert('L')
image = np.asarray(image, dtype="int32")
image = image[:,:,0]

edges = canny(tablets, sigma=5, low_threshold=30, high_threshold=60)
plt.imshow(edges, cmap="gray")
plt.show()
