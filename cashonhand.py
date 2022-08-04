# import Path , re , csv
from pathlib import Path
import csv

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





