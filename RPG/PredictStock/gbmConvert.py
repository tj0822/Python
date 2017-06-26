#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import matplotlib.pylab as plt

# Data load
data = pd.read_csv('data/KNIME_DataSet.csv')
data = pd.DataFrame.dropna(data, axis=0, how='any', thresh=None, subset=None, inplace=False)

# target, date 컬럼명 지정(predictors 아닌 컬럼들..)
target = 'Target'
date = 'DATE'

# prediction 컬럼에 사용할 지정
predictors = [x for x in data.columns if x not in [target, date]]

# X, Y data 설정
X = data[predictors]
Y = data[target]

# train set 설정(200개)
x_train, y_train = X.head(200), Y.head(200)

# test set 설정(train set 제외)
x_test,y_test  = X.tail(X.__len__()-200),Y.tail(X.__len__()-200)

# GBM parametor 설정(이부분을 R 소스와 유사하게 설정해주어야 하는데 잘 모르겠음.;;)
params = {'n_estimators': 6000, 'max_depth': 1, 'learning_rate': 0.01, 'warm_start': False, 'loss':'lad'}

# model fit
gbm0 = GradientBoostingRegressor(**params)
gbm0.fit(x_train, y_train)

# score list 생성(estimators 크기만큼)
test_score = np.zeros((params['n_estimators'],), dtype=np.float64)

bestY_pred = []

# iteration 하면서 가장 score(deviation값)가 낮은(?) 값이 최적값...인듯?
for i, y_pred in enumerate(gbm0.staged_predict(x_test)):
    test_score[i] = gbm0.loss_(y_test, y_pred)
    if i > 0 and test_score[i] < test_score[i-1]:
        bestY_pred = y_pred

# bestY_pred가 최적의 예측 데이터인듯...  bestY_pred를 예측 셋으로 넘겨서 사용하면 됨
print(bestY_pred)


########################################################################
# 여기서 부터는 옵션으로 plot 해보기

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, gbm0.train_score_, 'b-', label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-', label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')

plt.show()


# 영향력이 큰 feature찾기
feature_importance = gbm0.feature_importances_
# make importances relative to max importance
feature_importance = 100.0 * (feature_importance / feature_importance.max())
sorted_idx = np.argsort(feature_importance)
pos = np.arange(sorted_idx.shape[0]) + .5
plt.subplot(1, 2, 2)
plt.barh(pos, feature_importance[sorted_idx], align='center')
plt.yticks(pos, data[sorted_idx])
plt.xlabel('Relative Importance')
plt.title('Variable Importance')
plt.show()
