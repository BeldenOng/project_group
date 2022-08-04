#import Path, api, cashonhand , overheads, profit_loss
from pathlib import Path
import api, cashonhand , overheads, profit_loss
#create filepath for txt file
filepath_text = Path.cwd()/"summary_report.txt"
#add txt file to windows explorer
filepath_text.touch()

#open file path with .open()
with filepath_text.open(mode="w", encoding="UTF-8", newline = "\n") as summary_report:

    #defining the function
    def main():
    #Getting exchange rate value with our first API function
        forex=(api.api_function())
        
    #Printing out required statement of exchange rate with our second API function
        apisummary=str(api.api_statement(forex))
        summary_report.write(f"{apisummary}")

    #Identifying highest overheads
        overheadssummary=str(overheads.overheads(forex))
        summary_report.write(f"\n{overheadssummary}\n")

    #Identify cash deficit/surplus
        cashonhandloss = cashonhand.cashonhand(forex)
        #create condition if there is cash surplus 
        if cashonhandloss == []:
            summary_report.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        #create condition if there is cash deficit
        else:
            for i in range(len(cashonhandloss)):
                summary_report.write(f'[CASH DEFICIT] Day: {cashonhandloss[i][0]}, Amount: SGD{cashonhandloss[i][1]}\n')
        
    #Identifying net profit deficit/surplus
        pnlloss = profit_loss.profitandloss(forex)
        #create condition if there is profit surplus
        if pnlloss == []:
            summary_report.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
        #create condition if there is profit deficit
        else:
            for i in range(len(pnlloss)):
                summary_report.write(f'[PROFIT DEFICIT] Day: {pnlloss[i][0]}, Amount: SGD{pnlloss[i][1]}\n')
    #call back the function
    main()

    



