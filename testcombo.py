import pandas as pd
from pandas import DataFrame

import datetime
import pandas.io.data

#===============================================================================
# sp500 = pd.io.data.get_data_yahoo('%5EGSPC',
#                                   start = datetime.datetime(2000, 10, 1),
#                                   end = datetime.datetime(2015, 6, 16))
# #===============================================================================
#===============================================================================
# print sp500.head()  like R prints top 5
#===============================================================================
#===============================================================================
# sp500.to_csv('sp500_ohlc.csv')
#===============================================================================

df = pd.read_csv('vcwater.csv', index_col = 'custid')
#print df

df1 = df[(df['Attended'] == "No")]
print df1