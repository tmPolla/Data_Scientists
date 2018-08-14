# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:32:04 2018

@author: Polla
"""

# simple linear regression own solution
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values


# SPLITTING TRAIN AND TEST SET
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.score(X_test, y_test))


# PREDICTING TEH TEST SET RESULT
y_pred = regressor.predict(X_test)
print(y_pred)

# VISUALIZING THE TRAINING SET RESULT
plt.scatter(X_train, y_train, color='red')
plt.scatter(X_test, y_test, color='yellow')
plt.plot(X_train, regressor.predict(X_train))
#plt.plot(X_train, y_pred)
plt.title('Salary vs Experience (on training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()