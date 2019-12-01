from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# load iris data set
iris = load_iris()

# combine data and target
combined = [[*data, target] for data, target in zip(iris.data, iris.target)]
colors = ["red", "green", "blue"]
labels = ['sepal length', 'sepal width', 'petal length', 'petal width']

# plot
figure = plt.figure()

ax1 = figure.add_subplot(221, projection='3d')
ax2 = figure.add_subplot(222, projection='3d')
ax3 = figure.add_subplot(223, projection='3d')
ax4 = figure.add_subplot(224, projection='3d')

def scatter(ax, fields, data, marker, **kwargs):
    x = data[fields[0]]
    y = data[fields[1]]
    z = data[fields[2]]
    target = data[4]
    xLabel = labels[fields[0]]
    yLabel = labels[fields[1]]
    zLabel = labels[fields[2]]
    ax.scatter(x, y, z, c=colors[target], marker=marker)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)
    
for data in combined:
    scatter(ax1, [1,2,3], data, marker='o')
    scatter(ax2, [0,2,3], data, marker='o')
    scatter(ax3, [0,1,3], data, marker='o')
    scatter(ax4, [0,1,2], data, marker='o')
    

plt.show()

