from pathlib import Path
from statistics import mode
import api, cashonhand, overheads, profit_loss
filepath_text = Path.cwd()/"summary_report.txt"
filepath_text.touch()

def main():
    #Getting exchange rate value with our first API function
    forex=(api.api_function())

     #Printing out required statement of exchange rate with our second API function
    api.api_statement(forex)

    #Identifying highest overheads
    overheads.overheads()

    #Identifying cash deficit days, if no cash deficit days = cash surplus
    cashonhand.cashonhand(forex)

    #Identifying net profit deficit days, if no net profit deficit days = net profit surplus
    profit_loss.profitandloss(forex)
main()

with filepath_text.open(mode="w", encoding="UTF-8") as f:
    f.write(main())