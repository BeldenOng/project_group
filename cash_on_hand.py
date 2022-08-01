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


for i in range(len(list)-1):

    difference = int(list[i+1]) - int(list[i])
    if difference > 0 :
        print("higher")
    elif difference < 0:
        print("lower")



       
    
       
        
        #if line[1][second_day] > line[1][first_day]: 
            #print("hello") 
        #else:
            #print("bye") 
        