# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 20:31:50 2016

@author: John Plombon
"""
import google_intraday as goog_web
import pandas.io.data as web
import pandas as pd
import datetime

def IntradayStatics( symbol = 'iwm', day = 1, per_s = 60, date = '7_14_2016') :
    dcstr = "date = {!r}; symbol = {!r}; day = {!r}; period = {!r}sec".format( date, symbol, day, per_s)
    print dcstr
    
    sym_q_day_per_dt_close_pd = goog_web.GoogleIntradayQuote(symbol, per_s, day)
    f_name_day_per_sym_dt_pd = "C:\\Python27\\dev\\web\\GoogleFin\\{!s}_{!r}d_{!r}sbar_{!s}_close_pd.csv".format(symbol, day, per_s, date)
    print f_name_day_per_sym_dt_pd
    sym_q_day_per_dt_close_pd.write_csv_pd(f_name_day_per_sym_dt_pd)
    sym_q_day_per_dt_pd = pd.read_csv(f_name_day_per_sym_dt_pd)
    #sym_q_day_per_dt_pd[['close', 'high', 'low', 'open']].plot(figsize=(10, 5), grid=True)
    reg_len = len( sym_q_day_per_dt_pd[['open']] )
    dfOpen_date = sym_q_day_per_dt_pd[['open']]
    OpenValue_date = dfOpen_date.loc[0]
    
    ReturndfOpen_date = dfOpen_date - OpenValue_date
    #ReturndfOpen_date.plot(figsize=(10, 5), grid=True)
    
    # Return distribution parameters:
    Ret_sym_mean = ReturndfOpen_date['open'].mean()
    Ret_sym_max = ReturndfOpen_date['open'].max()  
    Ret_sym_min = ReturndfOpen_date['open'].min()  
    Ret_sym_median = ReturndfOpen_date['open'].median()  
    
    Ret_sym_std = ReturndfOpen_date['open'].std() 
    Ret_sym_skew = ReturndfOpen_date['open'].skew() 
    Ret_sym_kurt = ReturndfOpen_date['open'].kurt() 
    Ret_sym_var = ReturndfOpen_date['open'].var() 
    
    ReturndfOpen_date['open'].plot.hist(bins=50)
    sum_str = "Open = {!r}, reg ln = {!r}, mean = {:6.5f}, max = {:5.2f}, min = {:5.2f}, median = {:6.5f}".format( OpenValue_date, reg_len, Ret_sym_mean, Ret_sym_max, Ret_sym_min, Ret_sym_median )
    print sum_str
    sum2_str = "std = {:6.5f}, skew = {:6.5f}, kurt = {:6.5f}, var = {:6.5f}".format(Ret_sym_std, Ret_sym_skew, Ret_sym_kurt, Ret_sym_var)
    print sum2_str    
    
    month_str, day_str, year_str = date.rstrip().split('_')
    year_int = int(year_str)
    month_int = int(month_str)
    day_int = int(day_str)
    test_str = "year {!r}, month {!r}, day {!r}".format(year_int, month_int, day_int)
    print test_str
    #  Handle weekends and early part of the month
    calen_days = 5
    if day_int > calen_days :
        start_day = day_int-calen_days
    else:
        start_day = 31 - calen_days
        if month_int == 1:
            month_int = 12
        else:
            month_int = month_int - 1
    
    start_time = datetime.datetime(year_int, month_int, start_day)
    end_time = datetime.datetime(year_int, month_int, day_int)
    print "Start Time = {!r}".format( start_time )
    print "End Time = {!r}".format( end_time )
    GapData = web.DataReader(symbol, 'google', start_time, end_time)
    data_len = len(GapData['Open'])
    ValueOpen = GapData['Open'][data_len-1]
    ValuePreClose = GapData['Close'][data_len-2]
    ValueClose = GapData['Close'][data_len-1]
    GapValue_date = ValueOpen - ValuePreClose
    gap_value_str = "open = {:5.2f}, gap value = {:5.2f}, prev close = {:5.2f}, close = {:5.2f}".format(ValueOpen, GapValue_date, ValuePreClose, ValueClose )
    print gap_value_str
    #return OpenValue_date, reg_len, Ret_sym_mean, Ret_sym_max, Ret_sym_min, Ret_sym_median, Ret_sym_std, Ret_sym_skew, Ret_sym_kurt, Ret_sym_var
    return GapData



