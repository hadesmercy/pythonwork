#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:time-无产者
@file:数据处理.py
@time:2022/04/13
"""
import pandas as pd
import numpy as np



df = pd.read_csv("lianjia.csv")
print(df)
print(df.info())
print(df.describe())
print(len(df))

df.drop_duplicates(subset=['house_code'], keep='first', inplace=True)
print(len(df))
#
df.to_csv("beijing_4-14.csv")

# 虚拟人
# 天津项目二期
# 华源瑞丽
# HAIP平台
# 比赛项目



if __name__ == '__main__':
    pass

