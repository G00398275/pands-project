Programming and Scripting 2021 Project: Fisher's Iris Data Set
Lecturer: Andrew Beatty
Author: Ross Downey

PURPOSE
The purpose of this project is to research the well known Fisher's Iris Data set online, 
and to write documentation and Python code which investigates the data set appropriately.

RESEARCH
To initiate this project, the author began by searching the internet for resources and previous
investigations into this data set. There are a wide variety of resources and studies based on this
data set (a reference section is included below of the ones used for the purposes of this project).

BACKGROUND
In 1936 the British biologist and statistician Ronald Fisher published a paper titled 
'The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis'
in the scientific journal 'The Annals of Human Genetics'. In this paper Fisher developed a linear function to differentiate three different types of iris flower species (setosa, versicolor and virginica)
based on the lengths and widths of the flower's petals and sepals. Fisher evaluated this linear function based on data collected by the famed botanist Dr. Edgar Anderson. Anderson measured the lengths and widths of sepals and petals of fifty of each of the three types of iris. This yielded one hundred and fifty samples of data to work with and to help build Fisher's linear function. 
From these measurements Fisher was able to propose a model that could predict the species of a given iris based on the measurement of its sepals and petals.

SCOPE
The scope of this project is to download the Fisher / Anderson iris data set into Python, write a program in Python that outputs a summary of each variable to a single text file, saves a histogram of each variable to png files and outputs a scatter plot of each pair of variables. A text file summarising the project will also be created to clearly explain what is entailed in investigating the data set and how Python is adept at handling this data.

INITIAL ASSESSMENT
To begin assessing this data the author decided that the best place to start would be to mean all of the dimensions given in the data. To a student not familiar with data analytics it is not clear what way a project such as this should be initiated, it is felt that the average values would be a good place to start! Refer to mean.py included. Following this the author noted that the overall means, although useful, would not demonstrate the differences in petal/sepal dimensions. Consequently, the next step was to group the data by species (setosa / versicolor / virginica) and then determine the average sizes per group. A quick assessment of these means clearly shows that the virginica has the longest (average) sepal lengths, but the setosa has the widest (average) sepal widths. The versicolor has the longest petal lengths, but the virginica has the widest petals. 
This is an encouraging start to the assessment of this data. It is clearly evident, just from assessing the mean dimensions alone, that the three different species can, in some way, be distinguished from each other.
Further statistical evaluation is required, particularly in the area of standard deviations, quartile ranges etc., along with graphical representations (histograms, scatter plots etc.) to present and correlate the data.

REFERENCES
https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson35-3
https://tableconvert.com/?output=csv
