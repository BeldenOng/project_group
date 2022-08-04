# import Path , re , csv
from pathlib import Path
import re , csv
#filepath_COH = Path.cwd()/"csv.reports"/"cash-on-hand-usd.csv"


#open csv file using .open()
#with filepath_COH.open(mode="r", encoding="UTF-8", newline = '') as COH_file:
        #reader variable reader
        #reader = csv.reader(COH_file)
        #use next() to skip over the headers
        #next(reader)
        #create empty list
        #amount = []
        #day = []
        #create for loop for iteration
        #for line in reader:
            #append cash on hand numbers to empty list
            #amount.append(line[1])
            #append the respective days to empty list
            #day.append(line[0])

def cashonhand(forex):
    cwd = Path.cwd()
    cwd_csv = cwd/"csv.reports"/"cash-on-hand-usd.csv"
    day_amount = []
    with cwd_csv.open(mode = 'r', encoding = 'UTF-8', newline = '') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for data in csvreader:
            day_amount.append(data)
    cash_deficit = []
    for i in range(len(day_amount)):
        if i == 0:
            continue
        if day_amount[i][1] < day_amount[i-1][1]:
            deficit_amount = []
            deficit_amount.append("{:.2f}".format(float(day_amount[i][0])))
            deficit_amount.append("{:.2f}".format(forex*(int(day_amount[i-1][1]) - int(day_amount[i][1]))))
            cash_deficit.append(deficit_amount)
    return cash_deficit




#def cashonhand(forex):           
#define cashonhand()
        #CD = []
    #create for loop to iterate over all the days 
        #for i in range(len(amount)-1):
        #calculate the difference in Cash on hand amounts
            #difference = int(amount[i+1]) - int(amount[i])
        #creating condition when there is a cash deficit
            #if difference > 0 :
                #CD.append(amount[i+1])
                #return(f"[CASH DEFICIT] Day: {round(float(day[i+1]), 2)}, AMOUNT: SGD{round(float(amount[i+1]),1)*forex}]\n")
        #if (len(CD))== 0:
          #return("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY" )

        #calculate the difference in Cash on hand amounts
              
