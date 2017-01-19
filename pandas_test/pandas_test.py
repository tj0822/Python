#-*- coding:utf-8 -*-

import pandas as pd

data = pd.read_csv('data/convenient_store.csv')
print(data.head(10))

print(data.hourly_wage.describe())