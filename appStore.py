########################################################################################
# program: AppStore.py
# author: Mradul Mourya
# date: 03/24/2021
# Project: LM4 R cart modeling on a data set from Apple store 
# Reference: Professor Jones in class examples and textbook for this class
########################################################################################

# import all the libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
import random
import graphviz
plt.rcParams.update({'figure.autolayout': True})

# read into the file
apps = pd.read_csv("/Users/mmourya23/Documents/Intro to Data Science/LM4/AppleStore (1).csv")

# split the data into two parts, one is training data set and the other is test data set
appStore_train, appStore_test = train_test_split( apps, test_size = 0.25, random_state = 7 )

# to confirm that data was partioned correctly
apps.shape
appStore_train.shape
appStore_test.shape

# X stores the predictor variable
# none of the variables contain categorical data 
X = pd.concat( [ appStore_train['price'], appStore_train['user_rating'], appStore_train['size_bytes']],  axis=1 ) # predictor variable

# Y stores the target variable
Y = appStore_train['prime_genre']

# storing the unique categories from the target variable in class_name variable
class_names = appStore_train.prime_genre.unique()

# to count values (or frequencies) of each category
appStore_train['prime_genre'].value_counts()

# run the CART algorithm with 10 leaf nodes (as our tree would be big)
c50_01 = DecisionTreeClassifier(criterion="entropy", max_leaf_nodes=10).fit(X, Y)

# export the decision tree as .dot data by using export_graphviz library
dot_data = tree.export_graphviz(c50_01, out_file="c50_appStore.dot", feature_names = ['price','user_rating','size_bytes'] ,class_names=class_names, filled=True)

# again taking predictor variable from the test data and storing it to X
XT = pd.concat( [ appStore_test['price'], appStore_test['user_rating'], appStore_test['size_bytes']],  axis=1 )

# running prediction on the test data
predictions = c50_01.predict(XT)

# makes a copy of predictions variable to save the original data
XT_predictions = XT.copy()

# transfer the predicted data in the data frame
XT_predictions["predicted_genre"] = predictions

# transfer the actual data in the data frame
XT_predictions["actual_genre"] = appStore_test['prime_genre']