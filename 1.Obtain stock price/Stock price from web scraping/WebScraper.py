import requests
from bs4 import BeautifulSoup

'''
Function returns the price of a stock at the time of calling the function from yahoo finance.
'''

def stockScrape(code):
    #Correctly formats stock code
    if "^" in  code:
        code = code.replace("^", "%5E")
    return ("$"+(BeautifulSoup((requests.get("https://finance.yahoo.com/quote/"+code+"?p="+code)).content, "html.parser").find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text)) 



