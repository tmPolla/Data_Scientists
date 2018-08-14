# data prep

# import
dataset <- read.csv("Salary_Data.csv")
#dataset <- dataset[,2:3]


#SPLIT TRAIN AND TEST
#install.packages('caTools')
library(caTools)
set.seed(123)
split=sample.split(dataset$Salary, SplitRatio = 2/3)
train_set <-  subset(dataset, split==TRUE)
test_set <- subset(dataset, split==FALSE)


# FEATURE SCALING
# scale only the numeric columns and exclude the factor columns
# train_set[,2:3] = scale(train_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])
regressor <- lm(formula = Salary~YearsExperience,
                data=train_set)

y_pred <- predict(regressor, newdata = test_set)
y_pred


library(ggplot2)
ggplot()+
  geom_point(aes(x=train_set$YearsExperience, y= train_set$Salary),
             color='red')+
  geom_line(aes(x=train_set$YearsExperience, y=predict(regressor, newdata = train_set)))+
  ggtitle('Salary vs Experience on train set')+
  xlab('Year of Exp')+
  ylab('Salary')



ggplot()+
  geom_point(aes(x=test$YearsExperience, y= train_set$Salary),
             color='red')+
  geom_line(aes(x=train_set$YearsExperience, y=predict(regressor, newdata = train_set)))+
  ggtitle('Salary vs Experience on train set')+
  xlab('Year of Exp')+
  ylab('Salary')