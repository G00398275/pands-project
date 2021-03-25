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

iris = sns.load_dataset("iris")
sns.pairplot(iris, hue = 'species', height = 1, aspect = 0.8, kind='scatter', diag_kind='hist')
plt.show()

# Ref https://seaborn.pydata.org/generated/seaborn.pairplot.html

