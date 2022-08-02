#import requests
import requests

#create variable api_key
api_key = "JU5Q2GN41LOPWZ76"

#create url to variable url
url= f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=({api_key}'

#get url
response = requests.get(url)

#retrieve data with .json from response and save it as data
data = response.json()

# Use '.keys()' attribute to retrieve the keys of a dict
print(data.keys())



pmdata = (data["Realtime Currency Exchange Rate"])



CONVERSION = "[REAL TIME CURRENCY CONVERSION RATE]"

exchange_rate = float(pmdata['5. Exchange Rate'])

final_exchange_rate = (f"{CONVERSION} USD1 = SGD{round((exchange_rate),6)}")

print(final_exchange_rate)