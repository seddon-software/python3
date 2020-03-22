from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

def set_title(title):
    figure = plt.gcf()
    figure.canvas.set_window_title(title)

colors = ["red", "green", "blue", "black", "black"]
markers = ["o", "o", "o", "D", "D"]
sizes = [10, 10, 10, 100, 100]
labels = ['sepal length', 'sepal width', 'petal length', 'petal width']
target_names = {'setosa':0, 'versicolor':1, 'virginica':2}

iris_df = pd.read_csv("iris.csv")
iris_df["target"] = iris_df.apply(lambda row: target_names[row.species], axis=1, raw=True)
iris_df.drop(["species"], axis = 1, inplace = True)
iris1 = [4.1, 3.1, 1.8, 0.5, 3]
iris2 = [6.9, 3.5, 2.5, 2.5, 4]  
df = pd.DataFrame([iris1, iris2], columns = iris_df.columns) 
iris_df = iris_df.append(df)

# plot
figure = plt.figure(figsize=(12, 8))
set_title("red:0 green:1 blue:2 black:new")
ax1 = figure.add_subplot(221, projection='3d')
ax2 = figure.add_subplot(222, projection='3d')
ax3 = figure.add_subplot(223, projection='3d')
ax4 = figure.add_subplot(224, projection='3d')
        
def scatter(i, j, k, ax):
    def doit(row):
        n = int(row[4])          
        ax.scatter(row[i], row[j], row[k],   
                   c=colors[n], 
                   marker=markers[n],
                   s=sizes[n])

    ax.set_xlabel(labels[i])
    ax.set_ylabel(labels[j])
    ax.set_zlabel(labels[k])
    iris_df.apply(doit, axis=1, raw=True)
#     iris_df.apply(lambda row:ax.scatter(row[i], row[j], row[k],   
#                                         c=colors[int(row[4])], 
#                                         marker=markers[int(row[4])]), axis=1, raw=True)

scatter(0,1,2,ax1)
scatter(0,1,3,ax2)
scatter(0,2,3,ax3)
scatter(1,2,3,ax4)
plt.show()
