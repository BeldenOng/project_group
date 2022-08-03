# import Path , re , csv
from pathlib import Path
import re , csv
filepath_COH = Path.cwd()/"csv.reports"/"cash-on-hand-usd.csv"


#open csv file using .open()
with filepath_COH.open(mode="r", encoding="UTF-8", newline = '') as COH_file:
        #reader variable reader
        reader = csv.reader(COH_file)
        #use next() to skip over the headers
        next(reader)
        #create empty list
        amount = []
        day = []
        #create for loop for iteration
        for line in reader:
            #append cash on hand numbers to empty list
            amount.append(line[1])
            #append the respective days to empty list
            day.append(line[0])
            
#define cashonhand()
    #create for loop to iterate over all the days 
    for i in range(len(amount)-1):
        #calculate the difference in Cash on hand amounts
        difference = int(amount[i+1]) - int(amount[i])
        #creating condition when there is a cash deficit
        if difference < 0 :
          print(f"[CASH DEFICIT] Day: {round(float(day[i+1]), 2)}, AMOUNT: SGD{float(amount[i+1]) * forex}")

