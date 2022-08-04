from pathlib import Path
import api, cashonhand , overheads, profit_loss
filepath_text = Path.cwd()/"summary_report.txt"
filepath_text.touch()
with filepath_text.open(mode="w", encoding="UTF-8", newline = "\n") as summary_report:

    def main():
    #Getting exchange rate value with our first API function
        forex=(api.api_function())
        
     #Printing out required statement of exchange rate with our second API function
        api_statement_summary=str(api.api_statement(forex))
        summary_report.write(f"{api_statement_summary}")

    #Identifying highest overheads
        OVERHEADS_statement_summary=str(overheads.overheads())
        summary_report.write(f"\n{OVERHEADS_statement_summary}\n")

    #Identifying cash deficit days, if no cash deficit days = cash surplus
        cohlosses = cashonhand.cashonhand(forex)
        if cohlosses == []:
            summary_report.write(f'[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        else:
            for i in range(len(cohlosses)):
                summary_report.write(f'[CASH DEFICIT] Day: {cohlosses[i][0]}, Amount: SGD{cohlosses[i][1]}\n')
        
    #Identifying net profit deficit days, if no net profit deficit days = net profit surplus
        pnllosses = profit_loss.profitandloss(forex)
        if pnllosses == []:
            summary_report.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
        else:
            for i in range(len(pnllosses)):
                summary_report.write(f'[PROFIT DEFICIT] Day: {pnllosses[i][0]}, Amount: SGD{pnllosses[i][1]}\n')
    main()

    



