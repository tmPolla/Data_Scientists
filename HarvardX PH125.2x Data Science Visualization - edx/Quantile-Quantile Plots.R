#install.packages('dslabs')
# female and male hights
library(dslabs)
data(heights)

# create a vector with male hights
male <- heights$height[heights$sex=="Male"]

# create a vector with female hights
female <- heights$height[heights$sex=="Female"]

# create a sequence from 10% to 90% with 20% steps 
#so the 10th, 30th, 50th, 70th, and 90th percentile
seq_x <- seq(0.1, 0.9, 0.2)

# calculate the male and female percentiles
male_percentiles <- quantile(male, seq_x)
female_percentiles <- quantile(female, seq_x)

# create a dataframe to show the result in side-by-side
df <- data.frame(female=female_percentiles, male=male_percentiles)
df