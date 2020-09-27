import requests, json

BaseURL = 'https://paper-api.alpaca.markets'
OrdersURL = '{}/v2/orders'.format(BaseURL)
Headers = {"APCA-API-KEY-ID": "PKU31JDVN0AYRLMI1MEQ", "APCA-API-SECRET-KEY": "LVgw3y2RuffyDAMsjDR2EfscgsokGNTsuSEn3LUb"}

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }

    r = requests.post(OrdersURL, json=data, headers=Headers)
    return json.loads(r.content)
