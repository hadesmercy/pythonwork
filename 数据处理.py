#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

import pandas as pd
import numpy as np


df = pd.read_csv("lianjia.csv")
print(len(df))
df = df.dropna()
print(len(df))



# print(df.info())
# print(df['location1'].value_counts())
# print(df['room_type'].map(lambda str: re.findall(r'\d+室\d厅\d卫',str)))



# print(len(df))

#df.drop_duplicates(subset=['title','area','price','room_type'], keep='first', inplace=True)


df.to_csv("beijing_4-14.csv")




if __name__ == '__main__':
    pass

