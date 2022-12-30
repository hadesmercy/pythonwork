
#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:time-无产者
@file:草稿纸.py
@time:2022/01/25
"""
import pandas as pd

df = pd.read_csv("ttt.csv")
print(len(df))
df = df.dropna()
print(len(df))



# print(df.info())
# print(df['location1'].value_counts())



# print(len(df))
df.drop_duplicates(subset=['title'], keep='first', inplace=True)
print(len(df))

df.to_csv("A1ttt.csv")
