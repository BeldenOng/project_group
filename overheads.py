from pathlib import Path
import re , csv 
filepath_overheads= Path.cwd()/"csv.reports"/"overheads-day-45.csv"

with filepath_overheads.open(mode="r", encoding="UTF-8", newline = '') as overH_file:
    reader = csv.reader(overH_file)
    
    reader = csv.reader(overH_file)
    next(reader)
    list = []

    for line in reader:
        list.append(line)
        
    print(sorted(list, key = lambda x: x[1], reverse=True)[0])  
    


   