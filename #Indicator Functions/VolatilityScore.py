import requests
from bs4 import BeautifulSoup

'''
The Volatility Score is a function that calculates how far a given stocks value fluctuates in a day
as a percentage. Can be used to determine how stable a stocks value is.
'''

def volatilityScore(code):
    if "^" in code:
        code = code.replace("^", "%5E")
    Html = BeautifulSoup((requests.get("https://finance.yahoo.com/quote/"+code+"?p="+code)).content, "html.parser")
    Range = (((Html.find_all("div",{"class":"Bxz(bb) D(ib) Va(t) Mih(250px)!--lgv2 W(100%) Mt(-6px) Mt(0px)--mobp Mt(0px)--mobl W(50%)!--lgv2 Mend(20px)!--lgv2 Pend(10px)!--lgv2 BdEnd--lgv2 Bdendc($seperatorColor)!--lgv2"})[0]).find_all("table",{"class":"W(100%)"})[0]).find_all("tr")[4]).find("td",{"class":"Ta(end) Fw(600) Lh(14px)"}).text
    DailyHigh = float(Range.split("-")[1])
    DailyLow = float(Range.split("-")[0])
    Range = DailyHigh - DailyLow
    Open = (((Html.find_all("div",{"class":"Bxz(bb) D(ib) Va(t) Mih(250px)!--lgv2 W(100%) Mt(-6px) Mt(0px)--mobp Mt(0px)--mobl W(50%)!--lgv2 Mend(20px)!--lgv2 Pend(10px)!--lgv2 BdEnd--lgv2 Bdendc($seperatorColor)!--lgv2"})[0]).find_all("table",{"class":"W(100%)"})[0]).find_all("tr")[1]).find("td",{"class":"Ta(end) Fw(600) Lh(14px)"}).text
    Score = (Range / Open) * 100
    return Score
    
