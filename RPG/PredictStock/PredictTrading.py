#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.grid_search import GridSearchCV
from sklearn import cross_validation, metrics 
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pylab as plt
from datetime import datetime

# Data load
data = pd.read_csv('data/KNIME_DataSet.csv')
data = pd.DataFrame.dropna(data, axis=0, how='any', thresh=None, subset=None, inplace=False)
data["DATE"] = data.DATE.map(lambda x: pd.to_datetime(x))

# target, date 컬럼명 지정
target = 'Target'
date = 'DATE'

# ALGORITHM 변수
params = {'n_estimators': 6000, 'max_depth': 1, 'learning_rate': 0.01, 'warm_start': False, 'loss':'lad','alpha':0.95}
lagY = 1 # LAG Day
trainingDuration = 200 # Day

'''
# Boosting
LagY = 1 # Day
TrainingDuration = 200 # Day
#MyCtrl = trainControl(method = "timeslice", initialWindow = TrainingDuration, horizon = LagY, fixedWindow = TRUE)
#GBM_Static = train(Target ~ ., data = DFData, method = "gbm", preProc = c("center", "scale"), trControl = MyCtrl)
#MyTune = GBM_Static$bestTune
eGrid = expand.grid(interaction.depth = 1, n.trees = 6000, shrinkage = 0.1, n.minobsinnode = 10)
TotalIteration = nrow(DFIV) - TrainingDuration - LagY

GBM_Predict = ldply(1:TotalIteration, function(i){
  GBM_Model = train(Target ~ ., data =DFData[i:(i+TrainingDuration-1),], method = "gbm", preProc = c("center", "scale"), tuneGrid = eGrid)
  data.frame(DATE = DataSet$DATE[(i+TrainingDuration-1+LagY)]
             , Target = DFData$Target[(i+TrainingDuration-1+LagY)]
             , Target_hat = predict(GBM_Model, DFIV[(i+TrainingDuration-1+LagY),]))
})
'''
# prediction 컬럼에 사용할 지정78
predictors = [x for x in data.columns if x not in [target, date]]

# X, Y data 설정
XData = data[predictors]
YData = data[target]

dateList = []
priceList = []
predictList = []

# GBM parametor 설정
totalIteration = len(XData.index) - trainingDuration - lagY

for idx in range(2,totalIteration) :
    #train set creation
    trainData = data.loc[range(idx,(idx + trainingDuration - 1))]
    
    #gbm trade and predict
    gbmResult = GradientBoostingRegressor(**params)
    # print(gbmResult)
    # print(trainData[predictors])
    # print(trainData[target])
    gbmResult.fit(trainData[predictors], trainData[target])
    
    '''
    mse = mean_squared_error(trainData[predictors], gbmResult.predict(trainData[target])) 
    r2 = r2_score(trainData[predictors], gbmResult.predict(trainData[target])) 
    print("MSE: %.4f" % mse) 
    print("R2: %.4f" % r2) 
    '''
    #data summarize
    originData = data.loc[idx+trainingDuration-1+lagY]
    dateList.append(originData["DATE"])
    priceList.append(originData[target])
    predictList.append(gbmResult.predict(originData[predictors])[0])

                       
dfFinal = pd.DataFrame({"datetime" : dateList,"trade":priceList,"predict":predictList})
dfFinal.to_csv("PredictData_" +datetime.now().strftime("%Y%m%d%H%M%S")+ ".csv")
