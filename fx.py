import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import *


def convert_string_to_datetime(x):
    return (datetime.strptime(x, '%Y%m%d %H:%M:%S.%f'))


file_address = '/Users/Oliver/PyCharm/FX_app/test_data/EURUSD_test.csv'
df = pd.read_csv(file_address, names=['Symbol', 'Date_Time', 'Bid', 'Ask'], index_col=1, parse_dates=True,
                 converters={'Date_Time': convert_string_to_datetime})
PipPosition = 4
df['Spread'] = (df['Ask'] - df['Bid']) * 10 ** PipPosition
grouped = df.groupby('Symbol')
bid = grouped['Bid'].resample('1Min', how='ohlc')
ask = grouped['Ask'].resample('1Min', how='ohlc')
delta_ask = ask['high'] - ask['low']
delta_bid = bid['high'] - bid['low']
number_bars = len(ask)
width = 0
ax = plt.axes()
rects1 = ax.bar(np.arange(number_bars), delta_ask, width, color='r', bottom=ask['low'])

for opening, closing, bar in zip(ask['open'], ask['close'], rects1):
    x, w = bar.get_x(), 0.2

    args = {
    }

    ax.plot((x - w, x), (opening, opening), **args)
    ax.plot((x, x + w), (closing, closing), **args)

plt.show()
