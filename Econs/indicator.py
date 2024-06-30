import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import pandas_ta as ta


# 选择股票代码
ticker = 'Four'

# 下载过去一年的股票数据
stock_data = yf.download(ticker, period='1y')
stock_data.head()

# 获取数据
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')

# 计算 Volume Delta
data['Volume_Delta'] = data['Volume'].diff()

# 计算 n 天差 (这里以 n=5 为例)
n = 5
# 计算向前n天的差异
data[f'Close_{n}d_diff_forward'] = data['Close'] - data['Close'].shift(n)
# 计算向后n天的差异
data[f'Close_{n}d_diff_backward'] = data['Close'].shift(-n) - data['Close']


# 计算 n 天涨跌百分比
data[f'Close_pct_{n}'] = data['Close'].pct_change(n)

# 计算 CR 指标
data['CR'] = (data['Close'].rolling(window=n).sum() / data['Close'].rolling(window=n).max() - 1) * 100

# 计算最大值和最小值
data['Volume_Max'] = data['Volume'].rolling(window=n).max()
data['Volume_Min'] = data['Volume'].rolling(window=n).min()

# 计算 KDJ 指标
kdj = ta.stoch(data['High'], data['Low'], data['Close'])
data = data.join(kdj)

# 计算 SMA 指标
data['SMA'] = ta.sma(data['Close'], length=n)

# 计算 MACD 指标
macd = ta.macd(data['Close'])
data = data.join(macd)

# 计算 BOLL 指标
bollinger = ta.bbands(data['Close'])
data = data.join(bollinger)

# 计算 RSI 指标
data['RSI'] = ta.rsi(data['Close'])

# 计算 W%R 指标
data['WILLR'] = ta.willr(data['High'], data['Low'], data['Close'])

# 计算 CCI 指标
data['CCI'] = ta.cci(data['High'], data['Low'], data['Close'])

# 计算 ATR 指标
data['ATR'] = ta.atr(data['High'], data['Low'], data['Close'])

# 计算 DMA 指标
data['DMA'] = ta.sma(data['Close'], length=10) - ta.sma(data['Close'], length=50)

# # 计算 DMI 指标
# dmi = ta.dmi(data['High'], data['Low'], data['Close'])
# data = data.join(dmi)

# # 计算 TRIX 指标
# data['TRIX'] = ta.trix(data['Close'])

# 计算 VR 指标
data['VR'] = (data['Volume'] / data['Volume'].shift(1)).rolling(window=n).mean()





