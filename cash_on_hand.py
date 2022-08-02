from pathlib import Path
import re , csv 
filepath_COH = Path.cwd()/"csv.reports"/"cash-on-hand-usd.csv"



with filepath_COH.open(mode="r", encoding="UTF-8", newline = '') as COH_file:
        
        reader = csv.reader(COH_file)
        next(reader)
        amount = []
        day = []
        for line in reader:
            amount.append(line[1])
            day.append(line[0])
            
        print(amount)
        print(day)
            

def Cashonhand():
    for i in range(len(amount)-1):

        difference = int(amount[i+1]) - int(amount[i])
        if difference < 0 :
            print(f"[CASH DEFICIT] Day:{day[i+1]}, AMOUNT: SGD{amount[i+1]}]")
Cashonhand()
    






       
    
       
        
        
        