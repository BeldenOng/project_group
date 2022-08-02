import api , cashonhand , overheads , profit_loss

def main():
    forex = api.api_key
    cashonhand.cashonhand(forex)
    profit_loss.profitandloss(forex)
main()
