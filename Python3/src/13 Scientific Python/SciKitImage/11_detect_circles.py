import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from PIL import Image
import pandas as pd


def removeNearDuplicates(df):
    # remove near duplicates
    df = df.reset_index(drop=True)
    delta = 15
    duplicates = []
    for rowA in df.itertuples(name='A'):
        da = rowA._asdict()
        for rowB in df.itertuples(name='B'):
            db = rowB._asdict()
            if db['Index'] <= da['Index']: continue
            if abs(da['cx'] - db['cx']) < delta and abs(da['cy'] - db['cy']) < delta:
                duplicates.append(db['Index'])
    
    for d in set(duplicates):
        df = df.drop(d)
    
    df = df.reset_index(drop=True)
    return df

pd.set_option('display.max_rows', None)

# Load picture and detect edges
#image = Image.open("images/chips.png")
image = Image.open("images/tablets.jpg")
image.load()
#image = image.convert('L')
image = np.asarray(image, dtype="int32")
image = image[:,:,0]
#edges = canny(image, sigma=2, low_threshold=25, high_threshold=59)
edges = canny(image, sigma=5, low_threshold=30, high_threshold=60)


# Detect two radii
hough_radii = np.arange(33, 36, 1)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent 3 circles
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii, total_num_peaks=240)

df = pd.DataFrame(zip(cx, cy, radii))
df.columns = ['cx', 'cy', 'r']
df = df.sort_values(by=['cx', 'cy'])

df = removeNearDuplicates(df)
       

# Draw them
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4), dpi=72*2)
image = color.gray2rgb(image)

for index, row in df.iterrows():
    circy, circx = circle_perimeter(row['cy'], row['cx'], row['r'],
                                    shape=image.shape)

    plt.text(row['cx']-18, row['cy']+9, f"{index+1:2}", color="red", fontsize=6)

    r = range(-2, 3)
    for dx in r:
        for dy in r:
            image[circy+dy, circx+dx] = (0, 255, 0)    
 
print(df)
print(len(df))
ax.imshow(image, cmap=plt.cm.gray)
plt.show()



