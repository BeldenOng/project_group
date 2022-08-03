#import Path , re , csv
from pathlib import Path
import re , csv
from typing import overload 
#create variable filepath_overheads
filepath_overheads= Path.cwd()/"csv.reports"/"overheads-day-45.csv"


#open overheads csv file using .open()
with filepath_overheads.open(mode="r", encoding="UTF-8", newline = '') as overH_file:

    #create variable reader 
        reader = csv.reader(overH_file)
    #use next() to skip over header
        next(reader)
    #create empty list
        list = []

    #create for loop to iterate over the days 
        for line in reader:
        #append values to empty list
            list.append(line)


maximum = max(overhead)

def overheads():
    for i in range(len(overhead)-1):
        if overhead[i] == maximum:
            return(f"[HIGHEST OVERHEADS] {expense[i]} : {maximum}")

   