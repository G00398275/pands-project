# Programming and Scripting 2021 Project: Fisher's Iris Data Set; stats.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
# importing necessary modules

# Ref https://www.datacamp.com/community/tutorials/decision-tree-classification-python
# Ref https://www.hackerearth.com/practice/machine-learning/machine-learning-algorithms/ml-decision-tree/tutorial/
# Ref https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

myvar = pd.read_csv('irisDataSet.csv') # importing iris dataset

X = myvar.drop('species', axis=1) 
y = myvar['species']
# defining x and y cases, removing species from the x case as need numeric values only
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
# Setting the train and test cases, removing 25% of the data to use as the test case,
# Leaving 75% of the data to train the model
z = DecisionTreeClassifier()
z.fit(X_train, y_train)
y_pred = z.predict(X_test)
# Fitting the model using the decision tree classifier from sklearn module
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
# printing the confusion matrix and classification report to determine how accurate 
# is the model at predicting the species of iris 
