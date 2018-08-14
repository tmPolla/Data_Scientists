# data prep

# import
dataset <- read.csv("Data.csv")
dataset

# missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN=function(x) mean(x, na.rm=TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN=function(x) mean(x, na.rm=TRUE)),
                     dataset$Salary)

# ENCODING CATEGORICAL AND DUMMY VARIABLE
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No', 'Yes'),
                         labels = c(0,1))

#SPLIT TRAIN AND TEST
#install.packages('caTools')
library(caTools)
# set.seed(123) if we would like to see the same result
set.seed(123)
split=sample.split(dataset$Purchased, SplitRatio = 0.8)
train_set = subset(dataset, split==TRUE)
test_set = subset(dataset, split==FALSE)


# FEATURE SCALING
# scale only the numeric columns and exclude the factor columns
train_set[,2:3] = scale(train_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])