from pathlib import Path
<<<<<<< HEAD
import api, cashonhand, overheads, profit_loss
filepath_text = Path.cwd()/"summary_report.txt"
filepath_text.touch()
with filepath_text.open(mode="w", encoding="UTF-8", newline = "\n") as summary_report:

    def main():
    #Getting exchange rate value with our first API function
        forex=(api.api_function())
        
     #Printing out required statement of exchange rate with our second API function
        api_statement_summary=str(api.api_statement(forex))
        summary_report.write(f"\n{api_statement_summary}")

    #Identifying highest overheads
        OVERHEADS_statement_summary=str(overheads.overheads())
        summary_report.write(f"\n{OVERHEADS_statement_summary}")

    #Identifying cash deficit days, if no cash deficit days = cash surplus
        COH_statement_summary= str(cashonhand.cashonhand(forex))
        summary_report.write(f"\n{COH_statement_summary}")

    #Identifying net profit deficit days, if no net profit deficit days = net profit surplus
        PNL_statement_summary = str(profit_loss.profitandloss(forex))
        summary_report.write(f"\n{PNL_statement_summary}")
    main()

    
=======
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
>>>>>>> 4765c547e8ed69f0e236895640729702fdb98339
