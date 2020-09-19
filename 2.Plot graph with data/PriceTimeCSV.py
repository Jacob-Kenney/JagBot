import requests
from bs4 import BeautifulSoup
from WebScraper import stockScrape
import pandas
import datetime
import time

#Obtains stock price from webscraper and saves to CSV file
while 0 == 0:
    price = []
    col = []
    timeStamp = (datetime.datetime.now()).strftime("%Y - %m - %d %H:%M:%S")
    price.append(stockScrape("https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"))
    col = [timeStamp]
    col.extend(price)
    data=pandas.DataFrame(col)
    data=data.T
    data.to_csv("Price and time.csv", mode="a", header = False)
    print(col)

    
