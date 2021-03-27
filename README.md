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
Further statistical assessment of the Iris dataset was performed. This involved more research into capabilities of Python for handling datasets and outputting valuable information such as standard deviation, quartiles, minima / maxima etc. The author also discovered Python's ability to group the data by species and assess the data statistically in a grouped manner using the "pivot" function in the seaborn module.
Also, the "info" function was researched. This confirmed that the data did not require cleaning (no null values found), and that 150 values were present in the dataset, which was the required number. 
While this data has shown to be useful in terms of differentiating statistical values in terms of species, it has quickly become apparent that it is difficult to read and comprehend these numbers as the amount of data generated has become quite significant in a short space of time. Consequently, the next step in the analysis of this dataset is graphical representation. As the initial program has now become quite large it was decided to start graphical plots on a new program.

GRAPHICAL REPRESENTATIONS - BOXPLOTS
Boxplots of the Iris dataset were used in order to provide a clearer visual overview of the dimensions of the three different iris species. Boxplots are a graphical representation of range of data which show the mean, minimum, maximum, quartiles (and interquartile range).
The first box plot performed was of a plot of the different lengths and widths of petals and sepals of all 150 irises ungrouped. Inital observations from this are:

a) The sepals lengths are the largest numbers, the petals widths are the smallest.
b) The width of the petals gives the largest range, while the sepal widths give the smallest

This is also a good indicator that the variables measured give significant differences which could be exploited for the purposes of building a predictive model.

Further boxplots were also created but this time the data was grouped by species.
These boxplots give a better indication of sizes of petals / sepals in each species, which in turn could give a better idea of the defining characteristics of each type of iris. Greater knowledge of the defining dimensions of these iris species will help in building a model for prediciting a species from its sepal and petal sizes. The following observations were made from these boxplots:

1) Virginica has longer sepals than setosa, but are closer in length to versicolor.
2) Setosa has wider sepals than both versicolor and virginia (which are similar in sepal width).
3) Virginica has significantly longer petals than setosa, but are similar to versicolor.
4) Virginica also has significantly wider petals than setosa, and are slightly wider than versicolor.
5) Setosa has the narrowest range of all four dimensions which may make it easier to identify, particularly in petal length and width.

GRAPHICAL REPRESENTATION - HISTOGRAMS
Following the construction of boxplots and the data trends revealed by these, the next step was to construct histograms using the data for further analysis. A histogram arranges the data in groups (or bins / buckets) and then gives the frequency of this data in its respective groups. It is constructed with the groups on the x-axis and the frequency (represented by heights of bars) on the y-axis. Histograms can clearly indicate the spread of data and are give a good indication if the data is normally distributed or skewed. Matplotlib and Seaborn are two useful functions in Python for plotting histograms.
Initially, the histograms were constructed on the basis of their dimensions only. While useful in terms if visualisation of the dataset as a whole, this did not provide any assistance in building a predictive model.
The key take from these histograms is that both the sepal lengths and widths appear to be relatively normally distributed (the sepal widths appear particularly normally distributed). The petal dimensions, however, do not show any semblance of a normal distribution, and are both in fact bimodal. This infers that a predicitive model is more likely to be constructed through use of the sepal dimensions instead of the petal measurements. If data is normally distributed about the mean it implies that it is in stastical control and it is more favourable to predicitive models. The presence of skewed or bimodal histograms is more indicative of data that is not in statistical control.
On researching the internet for further histogram plots the author noted the "pairplot" function. This allowed plots to be constructed in appropriate groups (in this case species of iris). The resulting histogram and scatter plots gave a decent overview of the data which allowed for further assessment of the dataset. 
Observations from this pairplot incude:
1) Petal Length vs Petal Width seems to indicate a high level of regression for all species.
2) Sepal Length vs Sepal Width indicates the opposite.
3) Sepal Length vs Petal Length indicates good regression for versicolor and virginica, but not for setosa.
4) Sepal Length vs Petal Width also indicates a level of regression for versicolor and virginica but not for setosa.
5) Overall this pairplot indicates that the setosa species may not be suitable to build a predicitive model in this way but some dimensions of virginica and versicolor could be used. This should be support and/or confirmed by creating these scatter plots for each pair of data and calculating the regression value of each plot.

GRAPHICAL REPRESENTATION - HISTOGRAMS (GROUPED BY SPECIES)
The iris dataset was divided into species and each dimension was plotted on a histogram. 
This helps us to visualise the data in a better manner than the pairplot.
Observations made include:
1) Petal Length: Tends to be normally distributed with a noticeable difference between setosa and the other two species
2) Petal Width: Not as normally distributed but setosa also obviously different (shorter) than versica and versicolor
3) Sepal Length: All three species appear normally distributed but are close together (with some overlap)
4) Sepal Width: Also are tending towards normal distribution but are very close together. In the case of
versicolor and virginia the dimensions are nearly indistinguishable from each other.

GRAPHICAL REPRESENTATION - SCATTER PLOTS
A scatter plot is a plot of two variables against each other on two different axes, x and y. The linearity of the data (i.e an increase in one variable corresponds to an increase in the other) can be measured by calculating the regression value of a straight line drawn through the scatter plot data. The closer to one the regression value is the better the relative relationship (linearity) of the data.
Scatter plots will also start to informs us of actual mathematical terms we can use to interpret the data as opposed to visual indicators from boxplots and histograms.






REFERENCES
https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
https://en.wikipedia.org/wiki/Iris_flower_data_set#cite_note-anderson35-3
https://tableconvert.com/?output=csv
