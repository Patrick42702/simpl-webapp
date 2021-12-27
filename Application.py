import csv

"""
In this file, we are going to read from our 
weather csv file and parse the data for output
"""
filename = "weather.csv"#this is the name of the csv file

#In this function, we will open the csv file
#and read the contents, placing each line as an element into a new array
def readCSV(filename):
    fileContents = []
    with open(filename, newline = '', encoding = "utf-8") as f:
        for line in csv.DictReader(f):
            fileContents.append(line)
        return fileContents

def writeCSV():
    print("hello")

