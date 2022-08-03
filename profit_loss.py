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
<<<<<<< HEAD

        for line in reader:
                #append the amounts to empty list
            amount.append(line[4])
                #append the days to empty list
            day.append(line[0])
            
#define profitandloss()     

def profitandloss(forex):            
=======

        for line in reader:
                #append the amounts to empty list
            amount.append(line[4])
                #append the days to empty list
            day.append(line[0])

#define profitandloss()

def profitandloss(forex):
>>>>>>> 4765c547e8ed69f0e236895640729702fdb98339
#define cashonhand()
        PNL = []
    #create for loop to iterate over all the days 
        for i in range(len(amount)-1):
        #calculate the difference in Cash on hand amounts
            difference = int(amount[i+1]) - int(amount[i])
        #creating condition when there is a cash deficit
            if difference < 0 :
                PNL.append(amount[i+1])
<<<<<<< HEAD
                return(f"[PROFIT DEFICIT] Day: {round(float(day[i+1]), 2)}, AMOUNT: SGD{round(float(amount[i+1]) * forex,1)}]")
        if (len(PNL))== 0:
           return("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
<<<<<<< HEAD
=======
=======
                print(f"[PROFIT DEFICIT] Day: {round(float(day[i+1]), 2)}, AMOUNT: SGD{float(amount[i+1]) * forex}]")
        if (len(PNL))== 0:
           print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
>>>>>>> 4765c547e8ed69f0e236895640729702fdb98339
>>>>>>> b2e10492d0fb81b1ce24146ad81f5d767ca861d1
