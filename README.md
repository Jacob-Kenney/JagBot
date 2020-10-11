<h1 align="center"> JagBot V1.0.0 </h1> 
<h2 align = "center"> Description </h2>
<p> JagBot is a trading bot built entirely with python. It includes functionality for a vast range of features including; general market indicators, live stock market orders executed through an API, machine learning sentiment analysis, data visualisation, and ofcourse an algorithm which uses a combination of the listed features in order to make informed, profitable market trades.

JagBot was initially created for the purpose of learning, although we will continue to improve and adapt the program in order to, not only improve our programming skills, but also to make a product that provides a steady return on investment.<p>

<h3 align = "center"> Guide </h3>
<p>There are multiple functions that you can use to make the perfect algorithim. There are 2 notable functions, createOrder() and listen(). 

The createOrder() function lets you interact with the Alpaca API to make paper trades. It takes 3 arguments code, qty, and side. Code is simply the stock symbol such as TSLA for Tesla. The qty is the number of stocks that you wish to purchase and the side is whether you want to buy or sell. 

The second function is listen() which lets you get the askprice and bidprice for tracking the stock price. The listen() function takes simply 1 argument, code, which is the stock symbol. Note that when buying the stock you buy it at the latest askprice and when selling the stock you sell at the latest bidprice.

With these 2 functions we are confident that you can make spectacular algorithims! We implore you to try crazy thing such as machine learning or even sentiment analysis.
<p>
  
<h3 align = "center"> Future </h3>
<p> The project is fundamentally complete although there is huge opportunity for improvement available, in the future we would like to:
  
-Better follow market indicators in order to buy and sell at better times.
  
-Incorporate the machine learning sentiment anaylsis to make well informed trading decisions.
  
-Generally improve code.<p>
