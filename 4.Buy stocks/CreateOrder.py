import requests, json

'''
Function to create a market order of a stock using its code, the amount of stock ordering and
whether to buy or sell
'''
# Make sure to change your API Keys
BaseURL = 'https://paper-api.alpaca.markets'
OrdersURL = '{}/v2/orders'.format(BaseURL)
Headers = {"APCA-API-KEY-ID": "PKAIOPCAE58VF92T5C50", "APCA-API-SECRET-KEY": "PBgCZuNXPYH3Zx0VApc3gN56b9vid7kQRC0lKepJ"}

#Function to create a market order 
def createOrder(code, qty, side):
    data = {
        #Code is the code of the stock
        'symbol': code,
        #Quantity of stock order
        'qty': qty,
        #sell or buy
        'side': side,
        'type': "market",
        # This stands for good till cancel
        'time_in_force': "gtc"
    }

    r = requests.post(OrdersURL, json=data, headers=Headers)
    return json.loads(r.content)
    

BaseURL2 = "https://data.alpaca.markets/v1/last_quote/stocks/"
def listen(code):
    # We simply need to send the stock symbol and headers
    r = requests.get(BaseURL2 + code, headers = Headers)
    return json.loads(r.content)
