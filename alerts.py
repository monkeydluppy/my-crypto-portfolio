import csv
import sys
import pyttsx3
import time
import requests
from datetime import datetime


engine = pyttsx3.init()


# initialise all requirments for CMC
local_currency = 'USD'
local_symbol = '$'

api_key = 'Your-API-Key'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("ALERTS TRACKING...")
print()

already_hit_symbols = []

# read the csv file with your target data and store in a list
while True:
    with open("csv\my_alerts.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            symbol = line[0]
            amount = line[1]

            quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + \
                local_currency + '&symbol=' + symbol

            # send get request to get the data using API and store it in .json format
            request = requests.get(quote_url, headers=headers)
            results = request.json()

            # navigate the data and fetch and store all the required information
            currency = results['data'][symbol]

            name = currency['name']
            price = currency['quote'][local_currency]['price']

            # logic to say Alert alert alert when specified coins in csv file hits the target
            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                engine.say('ALERT ALERT ALERT')
                engine.say(name + ' hit  ' + amount)
                engine.runAndWait()
                sys.stdout.flush()

                # logic to give exact time when the price was hit
                now = datetime.now()
                current_time = now.strftime("%I:%M%p")
                print(name + ' hit ' + amount + ' at ' + current_time + '!')
                already_hit_symbols.append(symbol)

    print('...')
    time.sleep(10)
