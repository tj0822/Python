#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

trainData = pd.read_csv("../data/train.csv")
# trainData = pd.read_csv("RPG/Otto Group Product Classification Challenge/data/train.csv")


# trainData.boxplot(column=list(trainData[0:0])[1:3], by='target', vert=False)
# trainData.boxplot(column='target', by='feat_1', vert=False)
# trainData.boxplot(column='feat_1', by='target')


# trainData.loc[:,'feat_1':'target'].groupby('target').sum().boxplot(column=list(trainData[0:0])[1:94])