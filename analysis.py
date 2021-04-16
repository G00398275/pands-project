# Programming and Scripting 2021 Project: Fisher's Iris Data Set; dataOutput.py
# Lecturer: Andrew Beatty
# Author: Ross Downey

import pandas as pd 
from pandas import DataFrame
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

''' DATA SUMMARY'''

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

'''HISTOGRAMS'''

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

# Ref https://towardsdatascience.com/7-points-to-create-better-histograms-with-seaborn-5fb542763169
# Ref https://matplotlib.org/stable/gallery/color/named_colors.html
# Ref https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
# Ref https://stackoverflow.com/questions/15253897/stop-pylab-overlaying-plots

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
    plt.savefig('petalLengthHist.png')
    plt.gca().cla() # clearing data after each plot as overlapping onto subsequent ones

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
    plt.savefig('petalWidthHist.png')
    plt.gca().cla()

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
    plt.savefig('sepalLengthHist.png')
    plt.gca().cla()

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
    plt.savefig('sepalWidthHist.png')
    plt.gca().cla()

''' SCATTER PLOTS'''

# Ref https://seaborn.pydata.org/generated/seaborn.scatterplot.html
# Ref https://www.journaldev.com/39381/seaborn-scatter-plot
# Ref https://cmdlinetips.com/2019/04/how-to-specify-colors-to-scatter-plots-in-python/

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