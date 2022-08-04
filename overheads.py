from pathlib import Path
import csv

#create variable filepath_overheads
filepath_overheads= Path.cwd()/"csv.reports"/"overheads-day-45.csv"


#open overheads csv file using .open()
with filepath_overheads.open(mode="r", encoding="UTF-8", newline = '') as overH_file:

    #create variable reader 
    reader = csv.reader(overH_file)
    #use next() to skip over header
    next(reader)
    #create empty list
    expense= []
    overhead= []
    #create for loop to iterate over the days 
    for line in reader:
        #append values to empty list
        expense.append(line[0])
        overhead.append(line[1])

#location the maximum overhead 
maximum = max(overhead)

#defining function
def overheads():
    #create for loop to iterate over the datas
    for i in range(len(overhead)-1):
        #create condition if the value is maximum
        if overhead[i] == maximum:
            return(f"[HIGHEST OVERHEADS] {expense[i]} : {maximum}")

   