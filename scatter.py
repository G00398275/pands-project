# Programming and Scripting 2021 Project: Fisher's Iris Data Set; scatter.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

# Ref https://seaborn.pydata.org/generated/seaborn.scatterplot.html
# Ref 
# Ref 



import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# import iris dataset with Pandas
myvar = pd.read_csv("irisDataSet.csv")

for style in ['darkgrid']: # I find darkgrid is the easiest on the eyes!
    sns.set_style(style)
    sns.scatterplot(data = myvar, x="sepal_length", y="sepal_width", hue="species")
    plt.title('Sepal Length vs Sepal Width')
    plt.show()
