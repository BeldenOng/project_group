#import requests
import requests

#define api_function
def api_function():
    
    #create variable api_key
    api_key = "JU5Q2GN41LOPWZ76"

    #create url to variable url
    url= f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=({api_key}'


    #get url
    response = requests.get(url)

    #retrieve data with .json from response and save it as data
    data = response.json()

    #use '.keys()' attribute to retrieve the keys of a dict
    print(data.keys())

    #create variable pmdata
    pmdata = (data["Realtime Currency Exchange Rate"])

    #get exchange rate
    exchange_rate = float(pmdata['5. Exchange Rate'])

    #return exchange_rate to function
    return exchange_rate

#define api_statement()
def api_statement(forex):
    
    #create exchange rate statement
    final_exchange_rate_statement = (f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{(forex)}")
    
    #return exchange rate statement to function
    return(final_exchange_rate_statement)
   
   

