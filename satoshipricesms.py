import json
from urllib.request import urlopen
import time
from twilio.rest import Client
import os


ACCOUNT_SID = os.environ['TWILIO_ID']  
AUTH_TOKEN = os.environ['TWILIO_AUTH'] 

client = Client(ACCOUNT_SID, AUTH_TOKEN)


if __name__ == "__main__":

	coinbase_price_data = json.load(urlopen("https://api.coinbase.com/v2/prices/BTC-USD/spot/"))
	usd_bitcoin_price = float(coinbase_price_data['data']['amount'])

	print("The price is: " + str(usd_bitcoin_price))

	myMessage = client.messages.create(
	to=os.environ['PHONE_TO'],
	from_=os.environ['PHONE_FROM'], 
	body="The current bitcoin price is :" + " " + "1 BTC:" + str(usd_bitcoin_price) + "USD"
	)

	
	time.sleep(1 * 60)