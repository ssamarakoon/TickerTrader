import ta
import json
from urllib import request
import pandas as pd
import matplotlib.pyplot as plt

API_key = "7IGQGDVNF89WTOUS"

def trade(type , price, account):
    if type == 'buy':
        account[1] = (account[0] / price)
        account[0] = 0.0

    else:
        account[0] = (account[1] * price)
        account[1] = 0.0

# updates the value of the portfolio every day
def portfolioValue(price, account):
    if account[0] == 0.0:
        return account[1] * price
    else:
        return account[0]

def calculatePerformance(df, buyRange, sellRange, indicator):
    buy_signal = False
    reset_confirms = 6
    num_of_confirms = reset_confirms
    account = [100.0, 0.0]

    for index,row in df.iterrows():
        signal = row[indicator]
        close = row['close']

        if buy_signal == False and signal > buyRange:
            if num_of_confirms != 0:
                num_of_confirms -= 1
            else:
                trade('buy', close, account)
                buy_signal = True
                num_of_confirms = reset_confirms

        elif buy_signal == True and signal < sellRange:
            if num_of_confirms != 0:
                num_of_confirms -= 1
            else:
                trade('sell', close, account)
                buy_signal = False
                num_of_confirms = reset_confirms

        else:
            num_of_confirms = reset_confirms

        df.at[index, indicator + "_index"] = portfolioValue(close,account)


def main():

    ticker = input("Enter stock ticker:")
    response = request.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&outputsize=full&apikey=%s" %(ticker, API_key))
    data = json.loads(response.read())

    # load into DataFrame and clean the data
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'])
    df = df.T
    df = df.drop(['1. open', '2. high', '3. low', '5. adjusted close',
       '6. volume', '7. dividend amount', '8. split coefficient'], axis=1)
    df = df.reset_index()
    df = df.rename(columns={'index': 'date', '4. close': 'close'})
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    df['close'] = df['close'].astype('float')
    df = df.sort_values(by=['date'])
    df = df.reset_index(drop=True)

    # default n_fast=12, n_slow=26, n_signal=9
    df['MACD'] = ta.macd_diff(close=df['close'])

    # default n=14; have to normalize values to calculate performance
    df['RSI'] = ta.rsi(close=df['close'])
    df['RSI'] = df['RSI'].apply(lambda x: -x)

    df['MACD_index'] = ''
    df['RSI_index'] = ''

    calculatePerformance(df,0.0,0.0,"MACD")
    calculatePerformance(df,-30.0,-70.0,"RSI")

    plt.plot((df['date']), df['MACD_index'], label='MACD')
    plt.plot((df['date']), df['RSI_index'],  label='RSI')
    plt.title('Technical Indicator Performance')
    plt.legend
    plt.show()

if __name__ == '__main__':
    main()
