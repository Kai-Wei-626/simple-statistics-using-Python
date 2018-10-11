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

1. Use Minitab to create a fitted line plot of the data. (See Minitab Help Section - Creating a fitted line plot). 
Does a line do a good job of describing the trend in the data?
2. Interpret the r2 value. Does car speed explain a large portion of the variability in the average stopping distance? 
That is, is the r2 value large? Summarize how the title of this section is appropriate.
"""

import statsmodels.formula.api as smf
model = smf.ols('StopDist~Speed', data = df).fit()
print(model.summary())

















