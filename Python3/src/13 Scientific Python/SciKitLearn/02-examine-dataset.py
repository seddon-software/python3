from sklearn.datasets import load_iris
import pandas as pd
pd.set_option('display.width', None)        # None means all data displayed


# load iris data set
iris = load_iris()
names = {index:name for name,index in zip(iris.target_names, [0,1,2])}

# create feature and response dataframes
feature = pd.DataFrame(iris.data, columns=iris.feature_names)
response = pd.DataFrame(iris.target, columns=['target'])
response['target_names'] = response.apply(lambda row:names[row.target], axis='columns')

# combine dataframes
combined = pd.concat([feature, response], axis='columns', sort=False)
print(combined)

# print shapes
print("shape of feature matrix: {}".format(iris.data.shape))
print("shape of response matrix: {}".format(iris.target.shape))
