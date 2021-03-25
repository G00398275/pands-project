# Programming and Scripting 2021 Project: Fisher's Iris Data Set; boxplots.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# importing relevant modules

iris = sns.load_dataset("iris")# data from seaborn instead of csv file
ax = sns.boxplot(data=iris, orient="h", palette="Set3").set(xlabel = "cm",title = "Iris DataSet Boxplot")
plt.show()

# Ref https://seaborn.pydata.org/generated/seaborn.boxplot.html
# Ref https://www.python-graph-gallery.com/33-control-colors-of-boxplot-seaborn
# Ref https://stackoverflow.com/questions/37109021/changing-x-axis-labels-in-seaborn-boxplot
# Ref https://stackoverflow.com/questions/42406233/how-to-add-title-to-seaborn-boxplot


'''
Also need to boxplot the data in a grouped fashion to clearly see the range of data
for each species as opposed to the range of dimensions in the plot coded above
'''

iris = sns.load_dataset("iris")
iris.head()
sns.boxplot(x=iris["species"], y=iris["sepal_length"] ).set(ylabel = "cm", title = "Sepal Length")
plt.show()
sns.boxplot(x=iris["species"], y=iris["sepal_width"] ).set(ylabel = "cm", title = "Sepal Width")
plt.show()
sns.boxplot(x=iris["species"], y=iris["petal_length"] ).set(ylabel = "cm", title = "Petal Length")
plt.show()
sns.boxplot(x=iris["species"], y=iris["petal_width"] ).set(ylabel = "cm", title = "Petal Width")
plt.show()

# Ref https://pythonbasics.org/seaborn-boxplot/
