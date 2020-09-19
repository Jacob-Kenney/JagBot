import pandas
from alpha_vantage.timeseries import TimeSeries
import random

#The stock to be analysed
Symbol = "APPL"

def stockPrice(Symbol):
    #Randomly uses one of ten keys to allow a maximum 500 calls daily
    keys = random.choice(open("API.txt").read().splitlines())
    #Draws a table containing stock value per minute
    time = TimeSeries(key=keys, output_format="pandas")
    data = time.get_intraday(symbol=Symbol, interval="1min", outputsize="full")
    return data
