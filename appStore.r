########################################################################################
# program: AppStore.r
# author: Mradul Mourya
# Project: R cart modeling on a data set from Apple store 
########################################################################################

# install the packages for C50
install.packages("C50")
library('C50')

library(ggplot2)

# setting the path
setwd(dirname(rstudioapi::getSourceEditorContext()$path))

# read in the training data set as training_data
appStore_data <- read.csv("AppleStore (1).csv")

# set the seed for the random number generator for later use
set.seed(7)

# to determine the no. of records in the data set
n <- dim(appStore_data)[1]

# todetermine which records will be in the training data set via a random number generator.
train_ind <- runif(n) < 0.75

# partitioning the data sets
# one is training data set and other is test data set
appStore_train <- appStore_data[train_ind,]
appStore_test <- appStore_data[!train_ind,]

# factoring the predictor values since it contains categorical data
appStore_train$prime_genre <- factor(appStore_train$prime_genre)

# install rplot pacakage to run and visualize cart model
install.packages(c("rpart", "rpart.plot"))
library(rpart)

# formula = Taget ~ predictors
# The method = “class” input specifies that we want to use a classification (CART) model.
cart01 <- rpart(formula = prime_genre ~ price + user_rating + size_bytes, data = appStore_train, method = "class")

# Predict using the C5.0 Object
predict(object = cart01, newdata = appStore_test)

# look at the tree
# gives the probabilities 
summary(cart01)
