# import Path and csv
from pathlib import Path
import csv

#define cashonhand()
def cashonhand(forex):
    #locate file path
    filepath = Path.cwd()/"csv.reports"/"cash-on-hand-usd.csv"
    #create empty set 
    dayandamount = []
    #open csv file with open.()
    with filepath.open(mode = 'r', encoding = 'UTF-8', newline = '') as file:
        #create variable for reading of csv file
        csvreader = csv.reader(file)
        #use next() to skip over the header
        next(csvreader)
        #create for loop to iterate over the data
        for data in csvreader:
            #append data into empty list
            dayandamount.append(data)
    #create empty list
    cashdeficit = []
    #create for loop to iterate over all the indexes 
    for i in range(len(dayandamount)):
        #create condition if it is the first index
        if i == 0:
            continue
        #create condition if the amount is less than the previous day 
        if dayandamount[i][1] < dayandamount[i-1][1]:
            #create empty list 
            deficit = []
            #append day and amount to empty list defit
            deficit.append("{:.2f}".format(float(dayandamount[i][0])))
            deficit.append("{:.2f}".format(forex*(int(dayandamount[i-1][1]) - int(dayandamount[i][1]))))
            #append values to empty list cashdeficit
            cashdeficit.append(deficit)
    #return cashdeficit values to function
    return cashdeficit





