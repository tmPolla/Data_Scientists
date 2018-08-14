# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:28:45 2018

@author: Polla
"""

import pandas as pd

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
