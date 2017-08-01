#coding: utf-8
#火炉底架
import sys
sys.path.append('../')
from db.us_db import US_Database
import numpy as np
import pandas as pd
import datetime
from strategy_base import Strategy
import sklearn
from sklearn import linear_model
from util.plot_util import Plot_util
from util.test_util import Test_util
import statsmodels.tsa.stattools as ts
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

class Deep_point_strategy(Strategy):
    def __init__(self):
        self.date_range = 15
        self.db = US_Database()

    def deal_data(self,symbol):
        #find the biggest drop around 10 days
        start_date = datetime.datetime.today() - datetime.timedelta(self.date_range)
        ticker_data = self.db.get_ticker_by_id_not_consecutive_date(symbol,start_date=start_date).reset_index()
        ticker_data['delta'] = ticker_data['close'] - ticker_data['open']
        ticker_data['delta_pc'] = (ticker_data['close'] - ticker_data['open']) * 100 / ticker_data['open']

        if not ticker_data[ticker_data['delta_pc'] > 6].empty:
            #then we need to confirm the trend of drop
            pre_start_date = datetime.datetime.today
            X_train = ticker_data[]


            deep_index = ticker_data[ticker_data['delta_pc'] > 6].index[-1]
            if deep_index <= 2:
                #volume is so few and the change of price after deep is slience
                print(ticker_data.iloc[deep_index : ])





if __name__ == '__main__':
    db = US_Database()
    symbols = db.get_33_66_volume_by_day_symbol(20)
    dp = Deep_point_strategy()
    #loop
    # symbols.map(lambda x: dp.deal_data(x))
    for symbol in symbols:
        dp.deal_data(symbol)