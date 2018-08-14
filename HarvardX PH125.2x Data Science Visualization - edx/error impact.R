#install.packages('HistData')
library(HistData)
data(Galton)
x <- Galton$child

# mean of x
mean(x)

# median of x
median(x)

# standard deviation of x
sd(x)

# median absolute deviation of x
mad(x)

# create a wrong first value in x
x_with_error <- x
x_with_error[1] <- x_with_error[1]*10

# check the impact on the mean
# there is an impact
mean(x_with_error)-mean(x)

# check the impact on the sd
# there is an impact
sd(x_with_error)-sd(x)

# check the impact on the median
# no impact
median(x_with_error)-median(x)

# check the impact on the MAD
# no impact
mad(x_with_error)-mad(x)
