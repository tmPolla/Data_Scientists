# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 16:58:54 2018

@author: Polla
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv('Position_Salaries.csv')
# with the following code the result would be a list but we would like
# to use matrix
#X=dataset.iloc[:,1].values
# so create X as a matrix
X=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values


# SPLITTING TRAIN AND TEST SET
# we don't split the set because we have only 10 observation
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
lin_regressor = LinearRegression()
lin_regressor.fit(X,y)


from sklearn.preprocessing import PolynomialFeatures
poly_regressor = PolynomialFeatures(degree=2)
X_poly=poly_regressor.fit_transform(X)
lin_regressor_2 = LinearRegression()
lin_regressor_2.fit(X_poly, y)


poly_regressor_3 = PolynomialFeatures(degree=3)
X_poly_3=poly_regressor_3.fit_transform(X)
lin_regressor_3 = LinearRegression()
lin_regressor_3.fit(X_poly_3, y)

# Visualising the linear regression
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_regressor.predict(X), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the regression with degree=2
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_regressor_2.predict(X_poly), color = 'green')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the regression with degree=3
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_regressor_3.predict(X_poly_3), color = 'green')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the regression with degree=3 in more nice way
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_regressor_3.predict(poly_regressor_3.fit_transform(X_grid)), color = 'green')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# Predicting new results
lin_regressor.predict(6.5)

lin_regressor_2.predict(poly_regressor.fit_transform(6.5))