#-*- coding:utf-8 -*-
import pandas as pd
from matplotlib.mlab import PCA

data = pd.read_csv("../data/train.csv")
result = PCA(data)

print(result)