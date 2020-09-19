import requests
from bs4 import BeautifulSoup

#To change stock analysed change URL
URL = "https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"

def stockScrape(URL):
    #Returns all HTML from URL
    Html = BeautifulSoup((requests.get(URL) ).content,  "html.parser")
    #Returns price extracted from HTML
    price = "$" + (Html.find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text)
    return price

