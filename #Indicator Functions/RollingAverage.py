import requests
from bs4 import BeautifulSoup
import time

'''
Rolling average calculates the average stock price over a duration of time to reduce the affect of
anomalies on average.
'''

#Function scrapes yahoo finance for value of a given stock
def stockScrape2(code):
    if "^" in  code:
        code = code.replace("^", "%5E")
    return (BeautifulSoup((requests.get("https://finance.yahoo.com/quote/"+code+"?p="+code)).content, "html.parser")).find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text

#Function calculates rolling average for a stock over 10 minutes and saves to a csv file 
def findAverage(code):
    while 0 == 0:
        total, n= 0, 0
        while n < 10:
            price = float(stockScrape2(code))
            total += price
            n += 1
            average = total / n
            average = str(average)
            data = open("rolingAverage.csv", "w+")
            data.close()
            data = open("rollingAverage.csv", "a")
            data.write(average)
            data.close()
            time.sleep(60)

