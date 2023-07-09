# my-crypto-portfolio
This is a Python program that utilizes the Coin Market Cap API to fetch data and provide real-time information about my cryptocurrency portfolio. The program sends API requests to Coin Market Cap to retrieve cryptocurrency data, including prices, market cap, and other relevant information.

The program not only fetches data but also incorporates a feature that allows me to set specific sell targets for my holding coins. When a particular target is hit, the program generates alerts, ensuring that my target is met and it's time to sell!

# how to use 

clone this repo and edit csv files according to your crypto holding and targets (default value is provided if you don't want to change anything)

Make sure you have python installed, then using terminal/cmd navigate to the cloned folder and run the below command

    pip install -r requirements.txt

Go to alerts.py and portfolio.py and put your API key in api_key = 'Your-API-Key'

[Get your API key here.](https://coinmarketcap.com/api/)

*NOTE: It is recommended to use VS Code and launch it from there, if you dont like VS Code for some weird reason then you can use cmd/terminal too 

Now to see your portfolio, use the below command:

    python ./portfolio.py

To enable alerts, use the below command:

    python ./alerts.py
