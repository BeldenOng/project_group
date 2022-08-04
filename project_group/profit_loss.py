#importh Path , re , csv
from pathlib import Path
import csv

#define profitandloss function
def profitandloss(forex):
    #locate profit and loss csv
    filepath = Path.cwd()/"csv.reports"/"profit-and-loss-usd.csv"
    #create empty set
    values = []
    #open csv file with .open()
    with filepath.open(mode = 'r', encoding = 'UTF-8', newline = '') as file:
        #create variable for reading of csv file
        csvreader = csv.reader(file)
        #use next() to skip over the header
        next(csvreader)
        #create for loop to iterate over the data
        for data in csvreader:
            #append data to empty set values
            values.append(data)
    #create empty set PD
    PD = []
    #create for loop to iterate over the indexes
    for i in range(len(values)):
        #create condition if it is the first index
        if i == 0:
            continue
        #create condition if the amount is less than the previous day
        if values[i][4] < values[i-1][4]:
            #create empty list deficitamount 
            deficitamount = []
            #append day and amount to deficitamount
            deficitamount.append("{:.1f}".format(float(values[i][0])))
            deficitamount.append("{:.1f}".format(forex*(int(values[i-1][4]) - int(values[i][4]))))
            #append day and deficit amount to empty list PD
            PD.append(deficitamount)
    #return profitdeficit
    return PD