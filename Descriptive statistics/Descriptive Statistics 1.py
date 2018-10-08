'''
survival - Survival (0 = No; 1 = Yes)
class - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
name - Name
sex - Sex
age - Age
sibsp - Number of Siblings/Spouses Aboard
parch - Number of Parents/Children Aboard
ticket - Ticket Number
fare - Passenger Fare
cabin - Cabin
embarked - Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)
boat - Lifeboat (if survived)
body - Body number (if did not survive and body was recovered)

'''

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
os.chdir('/Users/kaiwei/Desktop/github/descriptive statistics')
df = pd.read_csv('titanic.csv')

# Infos
df.info()
df.isnull().sum()

#value_counts function, it gives an idea how the data distributed.
df['pclass'].value_counts()

#if we want to see what's percent of suvival people in each class, 
#clearly we can tell people with advanced class are more likely to survive
df.groupby('pclass')['survived'].mean()
'''
pclass
1.0    0.619195
2.0    0.429603
3.0    0.255289
'''

#df.describe() is also good function to generate quick stats
#can be used to check if extreme values exist
df.describe()

#sometimes we need to split value into different bucket. 
#For example, we can split age into 3 groups: child ,youth, youngAdult, MiddleAge, senior
#
ages = df['age']
bins = [0, 18, 25, 35, 60, 100]
group_names = ['children', 'youth', 'youngAdult', 'middleAge', 'Senior']
cats = pd.cut(ages, bins, labels = group_names)
#append the cats to the dataframe and named it 'age_group'
df['age_group'] = cats
'''
middleAge     289
youngAdult    281
youth         250
children      193
Senior         33
'''
#cut is a really useful function and there is also a function qcut which 
#cuts the data by quantiles


