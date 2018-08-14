import pandas as py
import quandl 

quandl.ApiConfig.api_key = "y3iPM8yQR6mNq3UABHyb"

df = quandl.get('WIKI/GOOGL')#df -- data frame

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

# percentage in the difference btw highest and lowest stocks on a given day
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] *100

# per day stock change percentage
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] *100

# volume is number of trades that happened that day--it gives volatility
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]
print(df.head())


