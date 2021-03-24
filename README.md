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
On the 24th March 2021 further statistical assessment of the Iris dataset was performed. This involved more research into capabilities of Python for handling datasets and outputting valuable information such as standard deviation, quartiles, minima / maxima etc. The author also discovered Python's ability to group the data by species and assess the data statistically in a grouped manner using the "pivot" function in the seaborn module.
Also, the "info" function was researched. This confirmed that the data did not require cleaning (no null values found), and that 150 values were present in the dataset, which was the required number. 
While this data has shown to be useful in terms of differentiating statistical values in terms of species, it has quickly become apparent that it is difficult to read and comprehend these numbers as the amount of data generated has become quite significant in a short space of time. Consequently, the next step in the analysis of this dataset is graphical representation. As the initial program has now become quite large it was decided to start graphical plots on a new program.

GRAPHICAL REPRESENTATIONS - BOXPLOTS
Boxplots of the Iris dataset were used in order to provide a clearer visual overview of the dimensions of the three different iris species. Boxplots are a graphical representation of range of data which show the mean, minimum, maximum, quartiles (and interquartile range).
The first box plot performed was of a plot of the different lengths and widths of petals and sepals of all 150 irises ungrouped. Inital observations from this are:

a) The sepals lengths are the largest numbers, the petals widths are the smallest.
b) The width of the petals gives the largest range, while the sepal widths give the smallest

This is also a good indicator that the variables measured give significant differences which could be exploited for the purposes of building a predictive model.

Further boxplots were also created but this time the data was grouped by species.



REFERENCES
https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson35-3
https://tableconvert.com/?output=csv
