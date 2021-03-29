# Programming and Scripting 2021 Project: Fisher's Iris Data Set; scatter.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

# Ref https://seaborn.pydata.org/generated/seaborn.scatterplot.html
# Ref https://www.journaldev.com/39381/seaborn-scatter-plot
# Ref https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/

import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# import iris dataset with Pandas
myvar = pd.read_csv("irisDataSet.csv")

colour_scheme = dict({'setosa':'seagreen', 'versicolor':'crimson', 'virginica': 'indigo'})
# Applying the same colour scheme as histograms for the three species
# 'hue' function differentiates each species from each other

# Sepal Length vs Sepal Width

for style in ['darkgrid']: # I find darkgrid is the easiest on the eyes!
    sns.set_style(style)
    sns.scatterplot(data = myvar, x="sepal_length", y="sepal_width", hue = 'species', 
    palette = colour_scheme)
    plt.title('Sepal Length vs Sepal Width')
    plt.show()

# Sepal Length vs Petal Width

for style in ['darkgrid']:
    sns.set_style(style)
    sns.scatterplot(data = myvar, x="sepal_length", y="petal_width", hue = 'species', 
    palette = colour_scheme)
    plt.title('Sepal Length vs Petal Width')
    plt.show()
    
# Sepal Length vs Petal Length

for style in ['darkgrid']: 
    sns.set_style(style)
    sns.scatterplot(data = myvar, x="sepal_length", y="petal_length", hue = 'species', 
    palette = colour_scheme)
    plt.title('Sepal Length vs Petal Length')
    plt.show()

# Sepal Width vs Petal Width

for style in ['darkgrid']: 
    sns.set_style(style)
    sns.scatterplot(data = myvar, x="sepal_width", y="petal_width", hue = 'species', 
    palette = colour_scheme)
    plt.title('Sepal Width vs Petal Width')
    plt.show()

# Sepal Width vs Petal Length

for style in ['darkgrid']: 
    sns.set_style(style)
    sns.scatterplot(data = myvar, x="sepal_width", y="petal_length", hue = 'species', 
    palette = colour_scheme)
    plt.title('Sepal Width vs Petal Length')
    plt.show()

# Petal Width vs Petal Length

for style in ['darkgrid']: 
    sns.set_style(style)
    sns.scatterplot(data = myvar, x="petal_width", y="petal_length", hue = 'species', 
    palette = colour_scheme)
    plt.title('Petal Width vs Petal Length')
    plt.show()

'''
Scatter plots only giving a visual indicator as to which dimensions are related
and could be used to build a predicitive model.
Next step is determine regression coefficients to help decide which sepal / petal
dimensions could be used for this model.
'''




