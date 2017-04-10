# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:30:22 2017

@author: miranda
"""

import pandas as pd

events = pd.read_csv('data_tables/storm_details.csv', 
                               index_col=7,
                               header = 0,
                               skiprows=100000)
events.head()