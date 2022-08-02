
import requests


api_key = "JU5Q2GN41LOPWZ76"

url= f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=({api_key}'

response = requests.get(url)

data = response.json()

print(data.keys())



pmdata = (data["Realtime Currency Exchange Rate"])



CONVERSION = "[REAL TIME CURRENCY CONVERSION RATE]"

exchange_rate = float(pmdata['5. Exchange Rate'])

final_exchange_rate = (f"{CONVERSION} USD1 = SGD{round((exchange_rate),6) }")


print(final_exchange_rate)