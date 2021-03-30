# Programming and Scripting 2021 Project: Fisher's Iris Data Set; stats.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import sys
# importing relevant modules


myvar = pd.read_csv("irisDataSet.csv") # Iris Data imported using Pandas
# format taken from w3schools tutorial on pandas

pd.set_option("display.precision", 3) # reducing number of decimals displayed

print(myvar.info()) # Ref https://www.geeksforgeeks.org/python-pandas-dataframe-info/
print ("\n") # adding space in code lines to read easier

#confirming 150 datapoints, also noted that there are no null values so no clean-up required

print("Sepal Length average is", myvar["sepal_length"].mean())
print("Sepal Width average is", myvar["sepal_width"].mean())
print("Petal Length average is", myvar["petal_length"].mean())
print("Petal Width average is", myvar["petal_width"].mean())
print ("\n") 


df = DataFrame(myvar, columns= ['sepal_length', 'sepal_width','petal_length', 'petal_width'])
# Adapted from https://datatofish.com/descriptive-statistics-pandas/
statValues = df.describe(include = 'all')
print (statValues)
print ("\n")

# Data needs to be averaged by group first before averaging by dimensions
#Reference: https://realpython.com/pandas-groupby/

species = myvar.groupby("species")

print(species.mean())
print ("\n")

pivotData = sns.load_dataset("iris") # need to import data using seaborn for pivoting
# this time loading the iris set from the seaborn module
 # Ref https://medium.com/@neuralnets/data-visualization-with-python-and-seaborn-part-1-29c9478a8700


print ("Sepal Length")
print(pivotData.pivot(columns='species', values='sepal_length').describe())
print ("Sepal Width")
print(pivotData.pivot(columns='species', values='sepal_width').describe())
print ("Petal Length")
print(pivotData.pivot(columns='species', values='petal_length').describe())
print ("Petal Width")
print(pivotData.pivot(columns='species', values='petal_width').describe())
print("Species")
print(pivotData.pivot(columns='species', values='species').describe())
# Ref https://cmdlinetips.com/2018/12/pivot-table-in-python-pandas/

'''
Now have good basis of statistical data. 
Can analyse and decide on best path to follow in terms of graphical plots from this
'''
import subprocess
outfile = open('test.txt','wt') #same with "w" or "a" as opening mode
outfile.write()
subprocess.Popen('ls',stdout=outfile)