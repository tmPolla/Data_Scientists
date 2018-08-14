# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:12:00 2018

@author: Polla
"""

import pandas as pd

dataset=pd.read_csv('Data.csv')
print(dataset)
X=dataset.iloc[:,:-1].values
print("X values are:")
print(X)
y=dataset.iloc[:,3].values
print("y values are:")
print(y)

# MIMSSING DATA
from sklearn.preprocessing import Imputer
imputer  = Imputer(missing_values='NaN', strategy= 'mean', axis=0)
imputer.fit(X[:,1:3])
X[:, 1:3]=imputer.transform(X[:, 1:3])
print("X values are after the imputer")
print(X)

#CATEGORICAL AND DUMMY VARIABLE
# Categorical variable transform to integer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X=LabelEncoder()
# country column
X[:,0] = labelencoder_X.fit_transform(X[:,0])
print("X values are after the first labelencoder")
print(X)
# create dummy variables
onehotencoder=OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
print("X values are after the first dummy transform")
print(X)

labelencoder_y=LabelEncoder()
y = labelencoder_y.fit_transform(y)


# SPLITTING TRAIN AND TEST SET
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)
#random_state=0 if we would like to see the same result


# FEATURE SCALING
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

