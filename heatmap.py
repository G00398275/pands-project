# Programming and Scripting 2021 Project: Fisher's Iris Data Set; heatmap.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

# Ref https://heartbeat.fritz.ai/seaborn-heatmaps-13-ways-to-customize-correlation-matrix-visualizations-f1c49c816f07
# Ref https://seaborn.pydata.org/generated/seaborn.heatmap.html
# Ref https://stackoverflow.com/questions/27037241/changing-the-rotation-of-tick-labels-in-seaborn-heatmap


import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris") # Loading iris dataset direct from Seaborn

sns.heatmap(iris.corr(), annot = True, vmin=-1, vmax=1, center= 0, cmap = 'coolwarm',
linewidths = 4, linecolor = 'black', cbar = False) # Formatting appearance
plt.title('Heatmap - Correlation Coefficients')
plt.yticks (rotation = 0) # Rotating y-axis label makes it easier to read
plt.show()

'''
Heatmap shows a good level of correlation between sepal length and both petal dimensions.
However, the best degree of correlation is between petal widths and lengths, value = 0.96.
'''