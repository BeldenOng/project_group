import api , cashonhand , overheads , profit_loss

def main():
    forex = api.exchange_rate
    cashonhand.cashonhand(forex)
    profit_loss.profitandloss(forex)
main()
