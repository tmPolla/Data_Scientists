library(dslabs)
data(heights)
x <- heights$height[heights$sex=="Male"]
avg <- mean(x)
stdev <- sd(x)
pnorm(72, avg, stdev)-pnorm(69, avg, stdev)

exact <- mean(x > 79 & x <= 81)
approx <- pnorm(81, mean(x), sd(x))-pnorm(79, mean(x), sd(x))
exact/approx


######## 
#estimation of proportion of adult men that are 7 feet tall or taller
1-pnorm(84, 69, 3)

########
# estimation of proportion of adult men that are 7 feet tall or taller 
# of 1 billion men
p<- 1-pnorm(84, 69, 3)
round(1000000000*p)


########
# estimation of proportion of adult men that are 7 feet tall or taller 
# of 1 billion men
# 10 NBA players
p<- 1-pnorm(84, 69, 3)
round(1000000000*p)