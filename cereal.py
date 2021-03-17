##################################
# program: AppleStore.py
# author: Mradul Mourya
# date: 03/15/2021
# purpose: CART data analysis, decision tree
###################################

import pandas as pd
from sklearn.model_selection import appStore_test_split
import random
app = pd.read_csv("/Users/mmourya23/Documents/Intro to Data Science/LM4/AppleStore (1).csv")

appStore_train, appStore_test = appStore_test_split(app, test_size = 0.25, random_state = 7)




