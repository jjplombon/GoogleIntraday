# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#  Attempt at debugging using IPython and Spyder
#  Under Debug menu | Debugging Control | Step [Ctrl F10] | Exit
#  Under Debug menu | Breakpoints | Set/Clear breakpint [F12]
#
#  Test IntradayAnalysis.py and google_intraday.py
#
# Created 07-27-2016
# Author John Plombon


import pandas as pd
import IntradayAnalysis as IA

symbol = 'qqq'
day = 1
per_s = 60
date = '7_27_2016'

sym_pd = IA.IntradayStatics(symbol, day, per_s, date)
#  sym_pd : is GapData, Open|High|low|close|Volume for 5 days...
sym_pd
