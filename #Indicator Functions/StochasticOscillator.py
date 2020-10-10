import requests
from bs4 import BeautifulSoup

'''
Stochastic Oscillator is a momentum indicator that shows the location of the close relative to the
high-low range. It follows the speed or the momentum of price. As a rule, the momentum changes
direction before price. As such, bullish and bearish divergences in the Stochastic Oscillator can be
used to foreshadow reversals.
'''

def stochasticOscillator(code):
    if "^" in code:
        code = code.replace("^", "%5E")
    Html = BeautifulSoup((requests.get("https://finance.yahoo.com/quote/"+code+"?p="+code)).content, "html.parser")
    Range = (((Html.find_all("div",{"class":"Bxz(bb) D(ib) Va(t) Mih(250px)!--lgv2 W(100%) Mt(-6px) Mt(0px)--mobp Mt(0px)--mobl W(50%)!--lgv2 Mend(20px)!--lgv2 Pend(10px)!--lgv2 BdEnd--lgv2 Bdendc($seperatorColor)!--lgv2"})[0]).find_all("table",{"class":"W(100%)"})[0]).find_all("tr")[4]).find("td",{"class":"Ta(end) Fw(600) Lh(14px)"}).text
    DailyHigh = float(Range.split("-")[1])
    DailyLow = float(Range.split("-")[0])
    CurrentValue = float(Html.find_all("div", {"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text)
    Average = ((CurrentValue - DailyLow) / (DailyHigh - DailyLow)) * 100
    return Average

