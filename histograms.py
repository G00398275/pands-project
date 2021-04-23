# Programming and Scripting 2021 Project: Fisher's Iris Data Set; histograms.py
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

myvar = pd.read_csv("irisDataSet.csv") # Iris Data imported using Pandas
# format taken from w3schools tutorial on pandas

for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(data = myvar, x = 'sepal_length', color = 'navy', kde = True,)
    plt.title ("Histogram of Sepal Lengths")
    plt.show()

for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(data = myvar, x = 'sepal_width', color = 'crimson', kde = True,)
    plt.title ("Histogram of Sepal Widths")
    plt.show()

for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(data = myvar, x = 'petal_length', color = 'indigo', kde = True,)
    plt.title ("Histogram of Petal Lengths")
    plt.show()

for style in ['darkgrid']:
    sns.set_style(style)
    sns.histplot(data = myvar, x = 'petal_width', color = 'seagreen', kde = True,)
    plt.title ("Histogram of Petal Widths")
    plt.show()

'''Plotting of histograms by dimension only, need to group into species first to 
gain more information from the histograms'''