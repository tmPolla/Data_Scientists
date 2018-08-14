# Ploynomial Regression

# import
dataset <- read.csv("Position_Salaries.csv")
dataset <- dataset[2:3]

# we don't split the set because of the less data there are only 10 records

# fitting linear regression to the dataset
lin_reg <-  lm(formula=Salary~.,
             data=dataset)

# fitting polynomial regression
# here the degree will be 2
dataset$Level2 <- dataset$Level^2
dataset$Level3 <- dataset$Level^3
dataset$Level4 <- dataset$Level^4
dataset$Level5 <- dataset$Level^5
poly_reg <- lm(formula=Salary~.,
               data=dataset)

# visualision the lin reg result
library(ggplot2)
ggplot()+
  geom_point(aes(x=dataset$Level, y=dataset$Salary),
              colour= 'red')+
  geom_line(aes(x=dataset$Level, y=predict(lin_reg,newdata = dataset)),
            colour= 'blue')+
  ggtitle('Linear Regression on Level and Salary')+
  xlab('Level')+
  ylab('Salary')

# visualision the ploynomial regression result
ggplot()+
  geom_point(aes(x=dataset$Level, y=dataset$Salary),
             colour= 'red')+
  geom_line(aes(x=dataset$Level, y=predict(poly_reg,newdata = dataset)),
            colour= 'blue')+
  ggtitle('Ploynomial Regression on Level and Salary')+
  xlab('Level')+
  ylab('Salary')

# predict new result with lin_reg
y_pred <- predict(lin_reg, data.frame(Level=6.5))

# predict new result with poly_reg
y_pred_poly <- predict(poly_reg, data.frame(Level=6.5,
                                            Level2=6.5^2,
                                            Level3=6.5^3,
                                            Level4=6.5^4,
                                            Level5=6.5^5))