
import pandas as pd # import pandas library


myvar = pd.read_csv("irisDataSet.csv") # Iris Data imported using Pandas
# format taken from w3schools tutorial on pandas

print("Sepal Length average is", myvar["sepal_length"].mean())
print("Sepal Width average is", myvar["sepal_width"].mean())
print("Petal Length average is", myvar["petal_length"].mean())
print("Petal Width average is", myvar["petal_width"].mean())


# Data needs to be averaged by group first before averaging by dimensions
#Reference: https://realpython.com/pandas-groupby/

species = myvar.groupby("species")

print(species.mean())

