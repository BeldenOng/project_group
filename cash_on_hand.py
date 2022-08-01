from pathlib import Path
import re , csv 
filepath_COH = Path.cwd()/"csv.reports"/"cash-on-hand-usd.csv"



with filepath_COH.open(mode="r", encoding="UTF-8", newline = '') as COH_file:
        
        reader = csv.reader(COH_file)
        next(reader)
        list = []
        for line in reader:
            list.append(line[1])
        
        print(list)

def cashonhand():
     
    for i in range(0,len(list)):

        difference = int(list[i+1]) - int(list[i])
        if difference > 0 :
            return("higher")
        elif difference < 0:
            return("lower")

print(cashonhand())

       
    
       
        
        #if line[1][second_day] > line[1][first_day]: 
            #print("hello") 
        #else:
            #print("bye") 
        