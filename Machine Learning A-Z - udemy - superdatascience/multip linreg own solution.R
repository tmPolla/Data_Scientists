# data prep

# import
dataset <- read.csv("50_Startups.csv")
dataset


# ENCODING CATEGORICAL AND DUMMY VARIABLE
dataset$State = factor(dataset$State,
                         levels = c('New York', 'California', 'Florida'),
                         labels = c(1,2,3))


#SPLIT TRAIN AND TEST
#install.packages('caTools')
library(caTools)
# set.seed(123) if we would like to see the same result
set.seed(123)
split=sample.split(dataset$Profit, SplitRatio = 0.8)
train_set = subset(dataset, split==TRUE)
test_set = subset(dataset, split==FALSE)



# Fttinh Multiple Linear Regression to the training set
# we have to specify all variable or use a single point
#regressor <- lm(formula = Profit~R.D.Spend+Administartion+MArketing.Spend+State)
regressor <- lm(formula = Profit~.,
                data=train_set)

# check the p-value (and a lot of other things)
summary(regressor)

# predict the test set result
y_pred <- predict(regressor, newdata = test_set)

# BACKWARD ELIMINATION
regressor <- lm(formula = Profit~R.D.Spend+Administration+Marketing.Spend+State,
                data = dataset)
summary(regressor)
# state2 has the highest p-value so we remove it
regressor <- lm(formula = Profit~R.D.Spend+Administration+Marketing.Spend,
                data = dataset)
summary(regressor)

# remove Administration
regressor <- lm(formula = Profit~R.D.Spend+Marketing.Spend,
                data = dataset)
summary(regressor)

# remove Marketing.Spend
regressor <- lm(formula = Profit~R.D.Spend,
                data = dataset)
summary(regressor)


# Automate version of the script
backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  return(summary(regressor))
}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)