# Programming and Scripting 2021 Project: Fisher's Iris Data Set; histogramsGrouped.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

# Ref https://towardsdatascience.com/7-points-to-create-better-histograms-with-seaborn-5fb542763169
# Ref https://matplotlib.org/stable/gallery/color/named_colors.html
# Ref https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0



import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Ref https://seaborn.pydata.org/generated/seaborn.pairplot.html
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue = 'species', height = 1, aspect = 0.8, kind='scatter', diag_kind='hist')
plt.show()

myvar = pd.read_csv("irisDataSet.csv") # Iris Data imported using Pandas
# format taken from w3schools tutorial on pandas


# Using "loc" function can group each set of data by species or whatever index required.
# Ref https://stackoverflow.com/questions/44890713/selection-with-loc-in-python
Setosa_Data = myvar.loc[myvar["species"]=="setosa"]
Versicolor_Data = myvar.loc[myvar["species"]=="versicolor"]
Virginica_Data = myvar.loc[myvar["species"]=="virginica"]

# References for histograms the same as histograms.py
# Petal Length Histogram
for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(Setosa_Data["petal_length"], color= "seagreen", kde = True)
    sns.histplot(Versicolor_Data["petal_length"], color= "crimson", kde = True)
    sns.histplot(Virginica_Data["petal_length"], color= "indigo", kde = True)
    plt.xlabel('Petal Length')
    plt.ylabel('Frequency')
    plt.title ('Petal Length - Grouped by Species')
    plt.legend(labels=['Setosa','Versicolor', 'Virginica'])
    plt.show()

# Petal Width Histogram
for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(Setosa_Data["petal_width"], color= "seagreen", kde = True)
    sns.histplot(Versicolor_Data["petal_width"], color= "crimson", kde = True)
    sns.histplot(Virginica_Data["petal_width"], color= "indigo", kde = True)
    plt.xlabel('Petal Width')
    plt.ylabel('Frequency')
    plt.title ('Petal Width - Grouped by Species')
    plt.legend(labels=['Setosa','Versicolor', 'Virginica'])
    plt.show()

# Sepal Length Histogram
for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(Setosa_Data["sepal_length"], color= "seagreen", kde = True)
    sns.histplot(Versicolor_Data["sepal_length"], color= "crimson", kde = True)
    sns.histplot(Virginica_Data["sepal_length"], color= "indigo", kde = True)
    plt.xlabel('Sepal Length')
    plt.ylabel('Frequency')
    plt.title ('Sepal Length - Grouped by Species')
    plt.legend(labels=['Setosa','Versicolor', 'Virginica'])
    plt.show()

# Sepal Width Histogram
for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(Setosa_Data["sepal_width"], color= "seagreen", kde = True)
    sns.histplot(Versicolor_Data["sepal_width"], color= "crimson", kde = True)
    sns.histplot(Virginica_Data["sepal_width"], color= "indigo", kde = True)
    plt.xlabel('Sepal Width')
    plt.ylabel('Frequency')
    plt.title ('Sepal Width - Grouped by Species')
    plt.legend(labels=['Setosa','Versicolor', 'Virginica'])
    plt.show()



