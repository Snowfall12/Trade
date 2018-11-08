'''
Created on 8 nov. 2018

@author: loicb
'''

import SupportFunctions as SF
import Data_Functions as DF
import pandas as pd
import datetime
from matplotlib import pyplot as plt

now=pd.to_datetime(datetime.datetime.now()).strftime('%Y-%m-%d')

# API key from Quandl to retrieve data
Tick="Wiki/AAPL"
Test=DF.GetData(Ticker=Tick, StartDate='2005-01-01', EndDate=now)
# Compute the daily returns of AAPl
Test=Test['Adj. Close'].pct_change(1)

# Apple returns over time plot
Test.plot()
plt.show()




