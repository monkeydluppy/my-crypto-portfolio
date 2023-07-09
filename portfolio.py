import csv
import requests
from prettytable import PrettyTable
from colorama import Back, Style

# initialise all requirments for CMC
local_currency = "USD"
local_symbol = "$"

api_key = "Your-API-Key"
headers = {"X-CMC_PRO_API_KEY": api_key}

base_url = "https://pro-api.coinmarketcap.com"


print("\nMY PORTFOLIO\n")


portfolio_value = 0.0

table = PrettyTable(["Assets", "Amount Owned", "Value",
                    "Price", "1h", "24h", "7d"])

# read the csv file with your portfolio data and store in lists
with open("csv\portfolio.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:

        symbol = line[0]
        amount = line[1]

        quote_url = base_url + "/v1/cryptocurrency/quotes/latest?convert=" + \
            local_currency + "&symbol=" + symbol

        # send get request to get the data using API and store it in .json format
        request = requests.get(quote_url, headers=headers)
        results = request.json()

        # navigate the data and fetch and store all the required information
        currency = results["data"][symbol]

        name = currency["name"]

        quote = currency["quote"][local_currency]

        hour_change = round(quote["percent_change_1h"], 1)
        day_change = round(quote["percent_change_24h"], 1)
        week_change = round(quote["percent_change_7d"], 1)

        price = quote["price"]

        value = float(price) * float(amount)

        portfolio_value += value

        # put some colors in the table to indicate profits and loss
        if hour_change > 0:
            hour_change = Back.GREEN + str(hour_change) + "%" + Style.RESET_ALL
        else:
            hour_change = Back.RED + str(hour_change) + "%" + Style.RESET_ALL

        if day_change > 0:
            day_change = Back.GREEN + str(day_change) + "%" + Style.RESET_ALL
        else:
            day_change = Back.RED + str(day_change) + "%" + Style.RESET_ALL

        if week_change > 0:
            week_change = Back.GREEN + str(week_change) + "%" + Style.RESET_ALL
        else:
            week_change = Back.RED + str(week_change) + "%" + Style.RESET_ALL

        price_string = "{0:,}".format(round(price, 2))
        value_string = "{0:,}".format(round(value, 2))

        # add all the information in the row of table
        table.add_row([name + " (" + symbol + ")", amount, local_symbol + value_string,
                      local_symbol + price_string, str(hour_change), str(day_change), str(week_change)])

# print the table
print(table)
print()


portfolio_value_string = "{:,}".format(round(portfolio_value, 2))

print("Total Portfolio Value: " + Back.GREEN +
      local_symbol + portfolio_value_string + Style.RESET_ALL)
print()
