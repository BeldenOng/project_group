from pathlib import Path
import re, csv 
filepath_COH = Path.cwd()/"csv.reports"/"cash-on-hand-usd.csv"


def cashonhand():
    with filepath_COH.open(mode="r", encoding="UTF-8", newline = '') as COH_file:
        global x
        reader = csv.reader(COH_file, delimiter = ',')
        next(reader)
        list = []
         
    
        for line in reader:
            list.append(line)
        
        print(list)
        
        if list[5][1] > list[4][1]: 
                return("over")
        else: 
                return("under")

print(cashonhand())
    
       
        
        #if line[1][second_day] > line[1][first_day]: 
            #print("hello")
        #else:
            #print("bye")
        