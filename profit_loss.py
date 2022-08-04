#importh Path , re , csv
from pathlib import Path
import re , csv


    #create variable filepath_PNL
filepath_PNL = Path.cwd()/"csv.reports"/"profit-and-loss-usd.csv"


#open csv using .open()
with filepath_PNL.open(mode="r", encoding="UTF-8", newline = '') as PNL_file:

        #create varibale reader
        reader = csv.reader(PNL_file)
        #use next() to skip over the headers
        next(reader)
        #create variable amount empty list 
        amount = []
        #create variable day empty list
        day = []
        #create for loop to iterate over the days

        for line in reader:
                #append the amounts to empty list
            amount.append(line[4])
                #append the days to empty list
            day.append(line[0])
            
#define profitandloss()     

def profitandloss(forex):            

        for line in reader:
                #append the amounts to empty list
            amount.append(line[4])
                #append the days to empty list
            day.append(line[0])

#define profitandloss()

def profitandloss(forex):
    cwd = Path.cwd()
    cwd_csv = cwd/"csv.reports"/"profit-and-loss-usd.csv"
    day_amount = []
    with cwd_csv.open(mode = 'r', encoding = 'UTF-8', newline = '') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for data in csvreader:
            day_amount.append(data)
    profit_deficit = []
    for i in range(len(day_amount)):
        if i == 0:
            continue
        if day_amount[i][1] < day_amount[i-1][1]:
            deficit_amount = []
            deficit_amount.append("{:.2f}".format(float(day_amount[i][0])))
            deficit_amount.append("{:.2f}".format(forex*(int(day_amount[i-1][1]) - int(day_amount[i][1]))))
            profit_deficit.append(deficit_amount)
    return profit_deficit