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



"""
































