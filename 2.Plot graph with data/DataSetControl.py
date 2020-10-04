import requests
from bs4 import BeautifulSoup
import pandas
import datetime
import time

'''
Function clears the created CSV file and creates headings for data
this function should be used before saving data for a new stock
'''
def initialiseData():
    data = open("Price and time.csv", "w+")
    data.close()
    data = open("Price and time.csv", "a")
    data .write(",Date and Time,Price")

'''
This functions saves a stocks value to a CSV file at time intervals given in seconds
'''
def createData(code,interval):
    while 0 == 0:
        price = []
        col = []
        timeStamp = (datetime.datetime.now()).strftime("%Y - %m - %d %H:%M:%S")
        #Pulls stock price live from yahoo finance
        if "^" in  code:
            code = code.replace("^", "%5E")
        value = BeautifulSoup(requests.get("https://finance.yahoo.com/quote/"+code+"?p="+code).content, "html.parser").find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text
        price.append(value)
        col = [timeStamp]
        col.extend(price)
        data=pandas.DataFrame(col)
        data=data.T
        #Prints date and time followed by price to a CSV file
        data.to_csv("Price and time.csv", mode="a", header = False)
        time.sleep(interval)
