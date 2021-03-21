'''Programming and Scripting 2021 Project: Fisher's Iris Data Set
Lecturer: Andrew Beatty
Author: Ross Downey'''

# This program imports the iris data set from iris.json
# Note: iris.json data copied from the following website: https://tableconvert.com/?output=json

import json
filename = "iris.json" # specifying file

def readDict():
    with open(filename) as f:
        return json.load(f) # loads dict from json file iris.json

irisData = readDict() # calling readDict function "somedict" to set up printing
print (irisData)