# TickerTrader
>Find annual returns of a stock ticker using techinical indicators

This application is designed to give the user the ability to backtest any publicly listed company in US financial markets based on two technical indicators, MACD and RSI.

## Using The Program
The application will first prompt the user to specify a company's historical data to backtest. The user will input the company's ticker symbol (should be on NYSE or NASDAQ) and in case the ticker symbol doesn't exist, the program will notify the user to re-input a different ticker. The program will output an line graph that shows the performance of using MACD vs. RSI. The graph starts at $100 initially and decreases/increases over time based off the trades. 

## The Technical Indicators
[MACD](https://www.investopedia.com/terms/m/macd.asp), Moving Average Convergence Divergence, is a trend indicator. It will be using the past 12 periods to build the fast EMA, the past 26 periods to build the slow EMA, and the past 9 periods to build the signal line. A buy execution will occur when the signal line is above the MACD for at least 6 periods, which indicates a bullish trend. A sell execution will ovver when the signal line is below the MACD for at least 6 periods, which indicates a bearish trend.

[RSI](https://www.investopedia.com/terms/r/rsi.asp), Relative Strength Indicator, is a momentum indicator. It will be using the past 14 periods of histocial data to generate an index value. A buy execution will occur when the RSI shows a consistent oversold signal with a reading of 30 or below for at least 6 periods. A sell execution will occur when the RSI shows a consistent overvalued signal, with a reading of 70 or above for at least 6 periods

## MSFT Example

![alt text](https://raw.githubusercontent.com/ssamarakoon/TickerTrader/tree/master/doc/figure.png)



