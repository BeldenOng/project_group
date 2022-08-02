#importh Path , re , csv
from pathlib import Path
import re , csv , api

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
def profitandloss():
    #create for loop to iterate over the all the days
    for i in range(len(amount)-1):
        #calculate the difference and store as variable 'difference'
        difference = int(amount[i+1]) - int(amount[i])
        #create condition of difference is less than 0
        if difference < 0 :
            print(f"[PROFIT DEFICIT] Day: {round(float(day[i+1]), 2)}, AMOUNT: SGD{(amount[i+1])}]")

#call back the function           
profitandloss()