import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import yfinance as yf

tsla = yf.Ticker('TSLA')
dowj = yf.Ticker('DJIA')

tsla.history(period='6mo')
dowj.history(period='6mo')

dowj_high = dowj.history(period='6mo').loc[:,'High']
tsla_high = tsla.history(period='6mo').loc[:,'High']

df = pd.DataFrame({'dowj_high':dowj_high,'tsla_high':tsla_high})
