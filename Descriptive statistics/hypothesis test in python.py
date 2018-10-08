#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 11:08:14 2018

@author: kaiwei

hypothesis test 1 : test if mean values of 2 samples are different

hypothesis test 2 : test if proportions  different

"""

"""
Hypothesis test 1 ----
Question: we are trygin to test whether a new, low-fat diet actually help obese people lose weight.
100 randomly assigned obese people are assigned to group 1 and put on the low fat diet. Another 100 
randomly assigned obese people are assigned to group 2 and put on a diet of approximately the same 
amount of food, but not as low in fat. After 4 months, the mean weight loss was 9.31 lbs for
group 1 (s = 4.67) and 7.40 lbs (s = 4.04) for group 2

@example question came from Khan Academy

"""
import numpy as np

mu1 = 9.31
mu2 = 7.4
std1 = 4.67
std2 = 4.04
n1 = 100
n2 = 100
# null hypothesis test: new diet does not help obese people lost weight
# H0: mu1 - mu2 = 0   H1: mu1 - mu2 > 0

# based on central limit therom, mean of the sample follows a normal distribution
# therefore the difference between 2 means of 2 samples follows a normal distribution as well
mu_difference = abs(mu1 - mu2)
var = std1**2/n1 + std2**2/n2
std_1_2 = np.sqrt(var)

# assume significance level is 5%, we want no more than 5% chance of incorrectly rejecting H0
alpha = 0.05
# critical value under 5%, z = 1.65
import scipy.stats as st
Z_value = st.norm.ppf(1-alpha)

# so if our value is larger than critical value, we can reject null hypo
# that means to get such value is less than 5%

Z_stats = mu_difference/std_1_2

# so if Z_stats > Z_value, we can reject null hyphthesis under 95% of times
# Quick wrap up to a function

def hypothesis_test_onetail(mu1, mu2, std1, std2, n1, n2, alpha):
    mu_difference = abs(mu1 - mu2)
    var = std1**2/n1 + std2**2/n2
    std_1_2 = np.sqrt(var)
    
    Z_value = st.norm.ppf(1-alpha)
    Z_score = (mu_difference - 0)/std_1_2
    if Z_score > Z_value:
        print('reject null hypothesis')
    else:
        print('fail to reject null hypothesis')
    return Z_score

hypothesis_test_onetail(9.31,7.3,4.67,4.64,100, 100, 0.05)

"""
hypothesis test 2 -----

there is a election coming up, and we are going to figure out if there
is a meaningful differece between the proportion of man and woman that 
are going to vote for a candidate. We randomly surveryed 1000 man and 1000 women.
642 men are going to vote for the candidate, 591 women will vote for the candidate.

@the example question came from Khan Academy
"""
p1 = 0.642
p2 = 0.591
n1 = 1000
n2 = 1000

# so the random variable that takes value 1 with probability p and the value 0 
# with probability q = 1- p, we call this random variable follows a bernoulli distribution

mu1 = p1
mu2 = p2
var1 = p1*(1-p1)
var2 = p2*(1-p2)

mu_difference = abs(mu1 - mu2)
std_1_2 = np.sqrt(var1/n1 + var2/n2) #standart deviation of sampling distribution

Z_score = (mu_difference-0)/std_1_2




























