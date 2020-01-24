from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

# load iris data set
iris = load_iris()

# combine data and target
combined = [[*data, target] for data, target in zip(iris.data, iris.target)]
colors = ["red", "green", "blue", "black", "black"]
labels = ['sepal length', 'sepal width', 'petal length', 'petal width']

# plot
figure = plt.figure()
set_title("red:0 green:1 blue:2 black:new")
ax1 = figure.add_subplot(221, projection='3d')
ax2 = figure.add_subplot(222, projection='3d')
ax3 = figure.add_subplot(223, projection='3d')
ax4 = figure.add_subplot(224, projection='3d')

def scatter(ax, fields, data):
    x = data[fields[0]]
    y = data[fields[1]]
    z = data[fields[2]]
    target = data[4]
    xLabel = labels[fields[0]]
    yLabel = labels[fields[1]]
    zLabel = labels[fields[2]]
    ax.scatter(x, y, z, c=colors[target], marker='o')
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)
    
iris1 = [4.1, 3.1, 1.8, 0.5, 3]
iris2 = [6.9, 3.5, 2.5, 2.5, 4]
for data in [*combined, iris1, iris2]:
    scatter(ax1, [1,2,3], data)
    scatter(ax2, [0,2,3], data)
    scatter(ax3, [0,1,3], data)
    scatter(ax4, [0,1,2], data)

plt.show()

