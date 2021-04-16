# Programming and Scripting 2021 Project: Fisher's Iris Data Set; dataOutput.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

''' Note: Running this program will output a statistical summary of iris dataset to
a file called variableSummary.txt
'''

# import iris dataset with Pandas
myvar = pd.read_csv("irisDataSet.csv")

pd.set_option("display.precision", 3) # reducing number of decimal places

with open ("variableSummary.txt", "wt") as f: # creating new txt file to summarise data(taken from lecture)
    f.write("Programming and Scripting 2021 Project: Fisher's Iris Data Set; variableSummary.py\nLecturer: Andrew Beatty\nAuthor: Ross Downey") 

with open ("variableSummary.txt", "at") as f: # 'a' to append (taken from lecture)
    f.write('\n')
    f.write('A summary of the four measurements provided (without grouping by species):')
    f.write('\n')
    f.write(str(myvar['sepal_width']))
    f.write('\n')
    f.write(str(myvar['sepal_length']))
    f.write('\n')
    f.write(str(myvar['petal_width']))
    f.write('\n')
    f.write(str(myvar['petal_length']))
    f.write('\n')

# Adding a summary of all data to .txt file

df = DataFrame(myvar, columns= ['sepal_length', 'sepal_width','petal_length', 'petal_width'])
# Adapted from https://datatofish.com/descriptive-statistics-pandas/
statValues = df.describe(include = 'all')
with open ("variableSummary.txt", "at") as f:
    f.write('\nA statistical summary of the four dimensions(without grouping by species):\n')
    f.write(str(statValues))

# Data needs to be averaged by group first before averaging by dimensions
#Reference: https://realpython.com/pandas-groupby/

species = myvar.groupby("species")
with open ("variableSummary.txt", "at") as f:
    f.write('\n\nThe mean values (grouped by species) are:\n')
    f.write(str(species.mean()))


pivotData = sns.load_dataset("iris") # need to import data using seaborn for pivoting
# this time loading the iris set from the seaborn module
 # Ref https://medium.com/@neuralnets/data-visualization-with-python-and-seaborn-part-1-29c9478a8700

with open ("variableSummary.txt", "at") as f:
    f.write("\nA statistical summary of the four dimensions(grouped by species):\n")
    f.write("\nSepal Length\n")
    f.write(str(pivotData.pivot(columns='species', values='sepal_length').describe()))
    f.write("\nSepal Width\n")
    f.write(str(pivotData.pivot(columns='species', values='sepal_width').describe()))
    f.write("\nPetal Length\n")
    f.write(str(pivotData.pivot(columns='species', values='petal_length').describe()))
    f.write("\nPetal Width\n")
    f.write(str(pivotData.pivot(columns='species', values='petal_width').describe()))
    f.write("\nSpecies\n")
    f.write(str(pivotData.pivot(columns='species', values='species').describe()))
# Ref https://cmdlinetips.com/2018/12/pivot-table-in-python-pandas/


with open ("variableSummary.txt", "at") as f:
    f.write("\n\nNow have good basis of statistical data.\nCan analyse and decide on best path to follow in terms of graphical plots from this")



