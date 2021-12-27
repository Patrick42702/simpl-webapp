import csv

"""
In this file, we are going to read from our 
weather csv file and parse the data for output
"""
filename = "weather.csv"#this is the name of the csv file

#In this function, we will open the csv file
#and read the contents, each line will be a dictionary, with
#header as keys and the data from the rows as values.
def readCSV(filename):
    fileContents = []
    with open(filename, newline = '', encoding = "utf-8") as f:
        for line in csv.DictReader(f):
            fileContents.append(line)
        return fileContents

data = readCSV(filename)#this is our global data variable

def mintemp_avg():#returns the average of minimum temps in the dataset
    avg_count: int = 0
    total_count: float = 0
    for dict in data:
        mintemp = float(dict["MinTemp"])
        total_count += mintemp
        avg_count += 1
    return round((total_count/avg_count), 2)

def maxtemp_avg():#returns the average of minimum temps in the dataset
    avg_count: int = 0
    total_count: float = 0
    for dict in data:
        mintemp = float(dict["MaxTemp"])
        total_count += mintemp
        avg_count += 1
    return round((total_count/avg_count), 2)

def rainfall_avg():
    avg_count: int = 0
    total_count: float = 0
    for dict in data:
        mintemp = float(dict["Rainfall"])
        total_count += mintemp
        avg_count += 1
    return round((total_count / avg_count), 2)

def evap_avg():
    avg_count: int = 0
    total_count: float = 0
    for dict in data:
        mintemp = float(dict["Evaporation"])
        total_count += mintemp
        avg_count += 1
    return round((total_count / avg_count), 2)