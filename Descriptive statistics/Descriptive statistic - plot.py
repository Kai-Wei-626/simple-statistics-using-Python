#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:38:49 2018

@author: kaiwei
"""

#descriptive stats 2 - plot
#this section is conncected with 'descriptive statistics -1.py'

import matplotlib.pyplot as plt

import os 
import pandas as pd
import numpy as np
os.chdir('~/descriptive statistics')
df = pd.read_csv('titanic.csv')

# I am going to plot 2 charts in this session
# 1. a distribution of age by histogram
# 2. a distribution of age with 3 classes by 3 histogram all in one figure.

# plot 1
# Source: https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f

def histogram(data, n_bins, cumulative=False, x_label = "", y_label = "", title = ""):
    _, ax = plt.subplots()
    ax.hist(data, bins = n_bins, cumulative = cumulative, color = '#539caf')
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)

# you will receive error if the data contains NAN values   
# therefore we can replace it with mean, but then the histgram will look bad, so maybe drop those rows?
df['age'] = df['age'].fillna(df['age'].mean())
df['age'].value_counts()
histogram(df['age'], n_bins = 50)   

# plot 2 - overlay age distributions on 3 classes
# drop the row contains nan this time
# I suddenly want to take a look the information of these rows with NAN
df.isnull().any() # return boolean value indicates whether each col has NaN

df = pd.read_csv('titanic.csv')

df_NAN = df[df['age'].isnull() == True] 
df_without_NAN = df[df['age'].isnull() == False] 

df_NAN.groupby('pclass')['survived'].mean()
df_without_NAN.groupby('pclass')['survived'].mean()

'''
df_without_NAN
pclass
1.0    0.637324
2.0    0.440613
3.0    0.261477
Name: survived, dtype: float64

df_NAN
pclass
1.0    0.487179
2.0    0.250000
3.0    0.240385
Name: survived, dtype: float64

looks like in the those rows with column age being null, the percent
of people in first class is less than the other group. 
'''

#ok lets go back to plot
# Create the plot
df_c1 = df_without_NAN[df['pclass'] == 1]['age']
df_c2 = df_without_NAN[df['pclass'] == 2]['age']
df_c3 = df_without_NAN[df['pclass'] == 3]['age']

_, ax = plt.subplots()
ax.hist(df_c1, bins = 50, color = 'r', alpha = 1, label = 'first class')
ax.hist(df_c2, bins = 50, color = 'b', alpha = 0.75, label = 'second class')
ax.hist(df_c3, bins = 50, color = 'y', alpha = 0.5, label = 'third class')


ax.set_ylabel('numbers of people')
ax.set_xlabel('age')
ax.set_title('dist of age in 3 classes')
ax.legend(loc = 'best')


# above is an overlay plot, let's try another way - seperate them but still in a operation
# the value 311 in add_subplot means 3 x 1 grid, the first plot
fig = plt.figure(figsize=(8,12))
ax1 = fig.add_subplot(311)
df_c1.hist(bins = 20)
ax1.set_xlabel('age')
ax1.set_ylabel('numbers of people')
ax1.set_title("first class")
ax1.set_xticks(np.arange(0, 80, 10))


ax2 = fig.add_subplot(312)
df_c2.hist(bins = 20)
ax2.set_xlabel('age')
ax2.set_ylabel('numbers of people')
ax2.set_title('second class')
ax2.set_xticks(np.arange(0, 80, 10))

ax3 = fig.add_subplot(313)
df_c3.hist(bins = 20)
ax3.set_xlabel('age')
ax3.set_ylabel('numbers of people')
ax3.set_title('third class')
ax3.set_xticks(np.arange(0, 80, 10))

# the result shows people in higher class are elder.
# We can also plot the age distribution based on if the passenger survived or not
