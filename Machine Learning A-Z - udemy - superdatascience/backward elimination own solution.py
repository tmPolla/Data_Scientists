# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:28:45 2018

@author: Polla
"""

import pandas as pd
import numpy as np

dataset=pd.read_csv('50_Startups.csv')

X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,4].values



#CATEGORICAL AND DUMMY VARIABLE
# Categorical variable transform to integer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
# country column
X[:,3] = labelencoder_X.fit_transform(X[:,3])
# create dummy variables
onehotencoder=OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()


#Avoiding the dummy variable trap
# drop the unnecessary 1 dummy variable
X=X[:,1:]

# SPLITTING TRAIN AND TEST SET
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)



# FEATURE SCALING
#from sklearn.preprocessing import StandardScaler
#sc_X=StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

# fit the mupliple linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict the test set result
y_pred = regressor.predict(X_test)

# barckward elimination
import statsmodels.formula.api as sm
X = np.append(arr=np.ones((50,1)).astype(int), values=X,axis=1)
X_opt = X[:, [0,1,2,3,4,5]]
# fit the full model with all possible predictors
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
# this will give back every important metrics of the regressor like p-value,coef etc.
# x1-x5 are the independent variables
# so we can choose the highest P-value
regressor_OLS.summary()
# X2 has the highest P-value so we remove this form the model
X_opt = X[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())
print(max(regressor_OLS.pvalues).astype(float))
# now the X1 has the highest P-value with 0.940 so we remove this
X_opt = X[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
# now the X2 has the highest wich is bogger than the SL = 0.05
X_opt = X[:, [0,3,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
# finally the X2 is the biggest with 0.06 which is bigger than SL
X_opt = X[:, [0,3]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()


#Automted versions

#Backward Elimination with p-values only:

import statsmodels.formula.api as sm
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        # choose the highest P value
        maxVar = max(regressor_OLS.pvalues).astype(float)
        # check pval bigger then sl?
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    # re-fit the model
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)


#Backward Elimination with p-values and Adjusted R Squared:

import statsmodels.formula.api as sm
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)
