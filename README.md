# TickerTrader
>Find annual returns of a stock ticker using technical indicators

This application is designed to give the user the ability to backtest any publicly listed company in US financial markets based on two technical indicators, MACD and RSI.

## Using The Program
The program will first prompt the user to specify a company's historical data to backtest. The user will input the company's ticker symbol (should be on NYSE or NASDAQ) and in case the ticker symbol doesn't exist, the program will notify the user to re-input a different ticker. The program will output an line graph that shows the performance of using MACD vs. RSI. The graph starts at $100 initially and decreases/increases over time based off the trades. 

## The Technical Indicators
[MACD](https://www.investopedia.com/terms/m/macd.asp), Moving Average Convergence Divergence, is a trend indicator. It will be using the past 12 periods to build the fast EMA, the past 26 periods to build the slow EMA, and the past 9 periods to build the signal line.

[RSI](https://www.investopedia.com/terms/r/rsi.asp), Relative Strength Indicator, is a momentum indicator. It will be using the past 14 periods of histocial data to generate an index value.

## The Trading Strategy
Historical data will be aggregated in daily format, using close prices of each day to calculate MACD and RSI. For the specified ticker, historical data will range from the earliest date that the AlphaVantage (market data provider) API can provide up to yesterday's date. The trading strategy for MACD is as follows: a buy is executed when the signal line is above the MACD for at least 6 periods, which indicates a bullish trend; a sell is executed when the signal line is below the MACD for at least 6 periods, which indicates a bearish trend. The trading strategy for RSI is as follows: A buy is executed occur when the RSI shows a consistent oversold signal with a reading of 30 or below for at least 6 periods. A sell is executed when the RSI shows a consistent overvalued signal, with a reading of 70 or above for at least 6 periods

## MSFT Example
Inputing 'MSFT', which is the ticker for Microsoft, shows that using the MACD trading strategy gives higher returns compared to the RSI trading strategy.
![alt text](https://github.com/ssamarakoon/TickerTrader/blob/master/doc/figure.PNG)

![alt text](https://github.com/ssamarakoon/TickerTrader/blob/master/doc/figure1.PNG)

Using a custom print output to find the end values. We see that trading with MACD brings an end value of $580.08 and RSI respectively of $334.85

![alt text](https://github.com/ssamarakoon/TickerTrader/blob/master/doc/figure2.PNG)

## Future Implementations
Using only a single technical indicator to determine when to buy/sell can be unreliable with the potential for false signals. For example a trend indicator like MACD might not address other technical aspects of market data such as volume, volatility, or momentum. These false signals can be reduced by using a combination of technical indicators such as MACD and RSI together to better determine buying/selling signals. 

Another problem that this application doesn't address is the risk-exposure of each strategy. MACD may have had the highest returns in the above example, but if it had open positions in the market longer than that for RSI, it exposes the portfolio to systematic (market specific) and unsystematic (company/industry specific) risk. One way to 

