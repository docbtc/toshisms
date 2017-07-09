import json
import urllib2
import time
from twilio.rest import TwilioRestClient
import os


ACCOUNT_SID = os.environ['TWILIO_ID']  
AUTH_TOKEN = os.environ['TWILIO_AUTH'] 

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

coinbase_price_data = json.load(urllib2.urlopen("https://api.coinbase.com/v2/prices/BTC-USD/spot/"))
usd_bitcoin_price = float(coinbase_price_data['data']['amount'])

print "The price is : " + str(usd_bitcoin_price)

print 'Sending Price'
			client.messages.create(
				to=os.environ['PHONE_TO'],
				from_=os.environ['PHONE_FROM'], 
				body="The current bitcoin price is : " + " " + "1 BTC:" + str(usd_bitcoin_price) + "USD")

time.sleep(1 * 60)