'''Programming and Scripting 2021 Project: Fisher's Iris Data Set
Lecturer: Andrew Beatty
Author: Ross Downey'''

# This program imports the iris data set

from sklearn.datasets import load_iris

iris = load_iris()
type (iris)

print (iris.feature_names)
print (iris.target)
print (iris.target_names)
print (iris.data)