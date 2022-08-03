#import requests
import requests

def api_function():
    #create variable api_key
    api_key = "JU5Q2GN41LOPWZ76"

    #create url to variable url
<<<<<<< HEAD
    url= f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=({api_key}'
=======
    url= f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=(%7Bapi_key%7D'
>>>>>>> 4765c547e8ed69f0e236895640729702fdb98339

    #get url
    response = requests.get(url)

    #retrieve data with .json from response and save it as data
    data = response.json()

    # Use '.keys()' attribute to retrieve the keys of a dict
    print(data.keys())



    pmdata = (data["Realtime Currency Exchange Rate"])

    exchange_rate = float(pmdata['5. Exchange Rate'])

<<<<<<< HEAD
    return exchange_rate
def api_statement(forex):
    final_exchange_rate_statement = (f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{(forex)}")
    return(final_exchange_rate_statement)
   
   
=======

    CONVERSION = "[REAL TIME CURRENCY CONVERSION RATE]"

    exchange_rate = float(pmdata['5. Exchange Rate'])

    return exchange_rate

def api_statement(forex):
    final_exchange_rate_statement = (f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{(forex)}")
    print(final_exchange_rate_statement)
>>>>>>> 4765c547e8ed69f0e236895640729702fdb98339

