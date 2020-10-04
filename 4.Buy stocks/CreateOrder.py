import requests, json

'''
Function to create a market order of a stock using its code, the amount of stock ordering and
whether to buy or sell
'''

BaseURL = 'https://paper-api.alpaca.markets'
OrdersURL = '{}/v2/orders'.format(BaseURL)
Headers = {"APCA-API-KEY-ID": "PKXW5PC7L420QGOQTQSE", "APCA-API-SECRET-KEY": "LiMU8o0MuuWQFlzOaAHJSbc0KOkQtTdqcuthJhTQ"}

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
        'time_in_force': "gtc"
    }

    r = requests.post(OrdersURL, json=data, headers=Headers)
    return json.loads(r.content)
    
