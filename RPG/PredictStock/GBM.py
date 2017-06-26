#-*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier         #GBM algorithm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation, metrics                   #Additional sklearn functions
from sklearn.grid_search import GridSearchCV                    #Perforing grid search
from sklearn.metrics import mean_squared_error

import matplotlib.pylab as plt
# from matplotlib.pylab import rcParams
# rcParams['figure.figsize'] = 12, 4

data = pd.read_csv('data/KNIME_DataSet.csv')
data = pd.DataFrame.dropna(data, axis=0, how='any', thresh=None, subset=None, inplace=False)
# print(train)

target = 'Target'
date = 'DATE'

def modelfit(alg, dtrain, predictors, performCV=True, printFeatureImportance=True, cv_folds=5):
    #Fit the algorithm on the data
    alg.fit(dtrain[predictors], dtrain[target])

    #Predict training set:
    dtrain_predictions = alg.predict(dtrain[predictors])
    dtrain_predprob = alg.predict_proba(dtrain[predictors])[:,1]

    print(dtrain_predictions)
    print(dtrain_predprob)

    #Perform cross-validation:
    if performCV:
        cv_score = cross_validation.cross_val_score(alg, dtrain[predictors], dtrain[target], cv=cv_folds, scoring='roc_auc')

    #Print model report:
        print('\nModel Report')
        print("Accuracy : %.4g" % metrics.accuracy_score(dtrain[target].values, dtrain_predictions))
        print("AUC Score (Train): %f" % metrics.roc_auc_score(dtrain[target], dtrain_predprob))

    if performCV:
        print("CV Score : Mean - %.7g | Std - %.7g | Min - %.7g | Max - %.7g" % (np.mean(cv_score), np.std(cv_score), np.min(cv_score), np.max(cv_score)))

    # Print Feature Importance:
    if printFeatureImportance:
        feat_imp = pd.Series(alg.feature_importances_, predictors).sort_values(ascending=False)
        feat_imp.plot(kind='bar', title='Feature Importances')
        plt.ylabel('Feature Importance Score')


#Choose all predictors except target & IDcols
predictors = [x for x in data.columns if x not in [target, date]]

X = data[predictors]
Y = data[target]
x_train, y_train = X.head(200), Y.head(200)
# print(x_train)
# print('')
# print(y_train)
# print('')
x_test,y_test  = X.tail(X.__len__()-200),Y.tail(X.__len__()-200)
# print(x_test)
# print('')
# print(y_test)

# print(predictors)
# gbm0 = GradientBoostingClassifier(learning_rate=0.1, subsample=0.7, min_samples_leaf=5, max_depth=1)
params = {'n_estimators': 6000, 'max_depth': 1, 'min_samples_split': 2, 'learning_rate': 0.1, 'loss': 'ls'}
gbm0 = GradientBoostingRegressor(**params)
# modelfit(gbm0, train, predictors)
gbm0.fit(x_train, y_train)

# print(train[predictors])
# print('============================')
# print(train[target])
# print('============================')
# print(gbm0)

dtrain_predictions = gbm0.predict(x_test)
# print(dtrain_predictions)
# print(mean_squared_error(y_test, dtrain_predictions))

test_score = np.zeros((params['n_estimators'],), dtype=np.float64)

bestY_pred = []
for i, y_pred in enumerate(gbm0.staged_predict(x_test)):
    # print(y_pred)
    test_score[i] = gbm0.loss_(y_test, y_pred)
    if i > 0 and test_score[i] < test_score[i-1]:
        bestY_pred = y_pred

print(bestY_pred)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, gbm0.train_score_, 'b-', label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-', label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')

plt.show()


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

# https://www.analyticsvidhya.com/blog/2016/02/complete-guide-parameter-tuning-gradient-boosting-gbm-python/
# param_test1 = {'n_estimators':range(20,81,10)}
# gsearch1 = GridSearchCV(estimator=gbm0, param_grid=param_test1, scoring='roc_auc', n_jobs=4,iid=False, cv=5)
# gsearch1.fit(x_train, y_train)
#
# search1_predictions = gsearch1.predict(x_test)
# print(search1_predictions)

# staged_predictions = gbm0.staged_predict(x_test)
# print(staged_predictions)
# print(mean_squared_error(y_test, staged_predictions))

# dtrain_predprob = gbm0.predict_proba(x_test)[:,1]


# print(len(dtrain_predictions))

# print(dtrain_predprob)
# print(len(dtrain_predprob))
