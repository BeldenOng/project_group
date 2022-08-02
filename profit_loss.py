from pathlib import Path
import re , csv 
filepath_PNL = Path.cwd()/"csv.reports"/"profit-and-loss-usd.csv"



with filepath_PNL.open(mode="r", encoding="UTF-8", newline = '') as PNL_file:
        
        reader = csv.reader(PNL_file)
        next(reader)
        amount = []
        day = []
        for line in reader:
            amount.append(line[4])
            day.append(line[0])
            
      
def profitandloss():
    for i in range(len(amount)-1):

        difference = int(amount[i+1]) - int(amount[i])
        if difference < 0 :
            print(f"[PROFIT DEFICIT] Day: {round(float(day[i+1]), 2)}, AMOUNT: SGD{amount[i+1]}]")
             
profitandloss()