4 assumptions of simple linear regression.
The mean of the response, E(Yi), at each value of the predictor, xi, is a Linear function of the xi.
The errors, εi, are Independent.
The errors, εi, at each value of the predictor, xi, are Normally distributed.
The errors, εi, at each value of the predictor, xi, have Equal variances (denoted σ2).

Questions resource: https://newonlinecourses.science.psu.edu/stat501/node/258/

"""Q1
The American Automobile Association has published data (Defensive Driving: Managing Time and Space, 1991) that
looks at the relationship between the average stopping distance ( y = distance, in feet) and the speed of a car
(x = speed, in miles per hour). The data set carstopping.txt contains 63 such data points.

1. Use Minitab to create a fitted line plot of the data. Does a line do a good job of describing the trend in the data?
2. Interpret the r2 value. Does car speed explain a large portion of the variability in the average stopping distance? 
That is, is the r2 value large? Summarize how the title of this section is appropriate.
"""
import statsmodels.api as sm
import pandas as pd
import os
os.chdir('...\\Desktop\\git')
datafile = "index.csv"
df = pd.read_csv(datafile)
df.head()


# For Q1
import matplotlib.pyplot as plt
plt.scatter(df.Speed, df.StopDist)
plt.plot(df.Speed, y_pred, color = 'r')
plt.show()
# in the plot, the variance of the stop distance increases as speed increases.

import statsmodels.formula.api as smf
model = smf.ols('StopDist~Speed', data = df).fit()
print(model.summary())
# the summary table has a high R square of 0.873


"""Q2 --- One data point can greatly affect the r2 value

The mccoo.txt data set contains data on the running back Eric McCoo's rushing yards (mccoo) for each game of the 
1998 Penn State football season. It also contains Penn State's final score (score).

Use Minitab to create a fitted line plot. Interpret the r2 value, and note its size.
Remove the one data point in which McCoo ran 206 yards. Then, create another fitted line plot on t
he reduced data set. Interpret the r2 value. Upon removing the one data point, what happened to the r2 value?
When a correlation coefficient is reported in research journals, there often is not an accompanying scatter plot. 
Summarize why reported correlation values should be accompanied with either the scatter plot of the 
data or a description of the scatter plot.
"""
datafile = "index_q2.csv"
df = pd.read_csv(datafile)

model = smf.ols('Score~McCoo', data = df).fit()
y_pred = model.predict(df.McCoo)
print(model.summary())

plt.scatter(df.McCoo, df.Score)
plt.plot(df.McCoo, y_pred, color = 'r')
plt.show()
# if we take that data point where McCoo ran 206 yards
df = df[df['McCoo'] != 206]
model = smf.ols('Score~McCoo', data = df).fit()
y_pred = model.predict(df.McCoo)
print(model.summary())

plt.scatter(df.McCoo, df.Score)
plt.plot(df.McCoo, y_pred, color = 'r')
plt.show()

# R square dropped from 0.249 to 0.079. Both of fail to reject null hypo of t test of coeefficient of predictor McCoo
#What conclusion can we draw from these data? Probably none! The main point of this example was to illustrate the impact of one data point on the r and r2 values. 
#One could argue that a secondary point of the example is that a data set can be too small to draw any useful conclusions.



"""Q3
Does a statistically significant P-value for H0 : β1 = 0 imply that β1 is meaningfully different from 0?

Recall that just because we get a small P-value and therefore a "statistically significant result" 
when testing H0 : β1 = 0, it does not imply that β1 will be meaningfully different from 0. 
This exercise is designed to illustrate this point. The data set practical.txt contains 1000 (x, y) data points.

1. Create a fitted line plot and perform a standard regression analysis on the data set. 
2. Interpret the r2 value. Does there appear to be a strong linear relation between x and y?
3. Use the Minitab output to conduct the test H0 : β1 = 0. (We'll cover this formally in Lesson 2, 
but for the purposes of this exercise reject H0 if the P-value for β1 is less than 0.05.)
What is your conclusion about the relationship between x and y?
4. Use the Minitab output to calculate a 95% confidence interval for β1. (Again, we'll cover this formally in Lesson 2,
but for the purposes of this exercise use the formula b1 ± 2 × se (b1).
Since the sample is so large, we can just use a t-value of 2 in this confidence interval formula.)
Interpret your interval. Suppose that if the slope β1 is 1 or more,
then the researcher's would deem it to be meaningfully different from 0. Does the interval suggest, 
with 95% confidence, that β1 is meaningfully different from 0?
5. Summarize the apparent contradiction you've found. What do you think is causing the contradiction?
And, based on your findings, what would you suggest you should always do, whenever possible, when analyzing data?
"""

#1
datafile = "index_q3.csv"
df = pd.read_csv(datafile)
df.head()

model = smf.ols('y ~ x', data = df).fit()
y_pred = model.predict(df.x)
model.summary()


plt.scatter(df.x, df.y)
plt.plot(df.x, y_pred, color = 'r')
plt.show()

# This fitted line has a slope with 0.0998 associated wiht a p value less than 0.01.

#2
r2 = 0.243
#3
p_value < 0.05, signicant
#4
CI = [.089, 0.111]
#5





#### Solution
https://newonlinecourses.science.psu.edu/stat501/node/392/
























