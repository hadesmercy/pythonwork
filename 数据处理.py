#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

import pandas as pd
import numpy as np


df = pd.read_csv("lianjia_lz.csv")
print(len(df))
df = df.dropna()



print(len(df))


df.drop_duplicates(subset=['title','area','price','room_type'], keep='first', inplace=True)


print(len(df))

df.to_csv("lianjia_lz_clean.csv")




if __name__ == '__main__':
    pass

