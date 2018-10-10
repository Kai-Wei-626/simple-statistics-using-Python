"""
Questions are from https://onlinecourses.science.psu.edu/stat500/node/69/

import scipy.stats as st
st.norm.cdf(1.65) will return 0.95 
st.norm.ppf(1 - alpha) will return the z-critical value such as st.norm.ppf(0.95) will return 1.65
"""

"""Q1
  A survey of National Federation of Independence Business (NFIB) indicates that small businesses intended to increase their hiring 
  as well as their capital expenditures during 1986 as compared with 1985. Suppose that, as part of a follow-up survey by NFIB, 
  20 small businesses, randomly chosen from the NFIB's list of 2,100 companies, show an average hiring from 1985 equal to
  3.2 new employees per firm and a standard deviation of 1.5 hires. A random sample of 30 small businesses taken at the end of 1986 
  shows an average of 5.1 new hires and a standard deviation of 2.3 hires. At the α = 0.01
  level of significance, can you conclude that average hiring by all small businesses in 1986 increased as compared with 1985?
"""
import numpy as np
import scipy.stats as st
# H0: mu1 - mu2 = 0
mu1, mu2 = 3.2, 5.1
std1, std2 = 1.5, 2.3
n1, n2 = 20, 30
mu_difference = abs(mu1 - mu2)
var = std1**2/n1 + std2**2/n2
std_1_2 = np.sqrt(var)
alpha = 0.01
# critical value under 1%, z = 2.32
Z_value = st.norm.ppf(1-alpha)
Z_stats = (mu_difference - 0)/std_1_2
"""
Z-stats(z-score) = 3.5 and Z-value = 2.32, since Z-stats > Z-value, we conclude to reject null hypo under 5% level of significance
"""


"""Q2
It is known that the average stay of tourists in Hong Kong hotels has been 3.4 nights. 
A tourism industry analyst wanted to test whether recent changes in the nature of tourism to 
Hong Kong have changed from this past average. The analyst obtained the following random sample of the number of nights 
spent by tourists in Hong Kong hotels: 5, 4, 3, 2, 1, 1, 5, 7, 8, 4, 3, 3, 2, 5, 7, 1, 3, 1, 1, 5, 3, 4, 2, 2, 2, 6, 1, 7. 
Conduct the test using the 0.05 level of significance.
"""
# test of a hypothesis about a population mean mu. H0: average stay of tourists in HK is 3.4 nights
data =[5, 4, 3, 2, 1, 1, 5, 7, 8, 4, 3, 3, 2, 5, 7, 1, 3, 1, 1, 5, 3, 4, 2, 2, 2, 6, 1, 7]
mu = np.mean(data)
std_sample = np.std(data)
std_pop = std_sample
n = len(data)
std_of_sampling_dist = std_sample/np.sqrt(n)

t_score = abs(mu-3.4)/std_of_sampling_dist
# since t score is lower than 1.96, we fail to reject Null hypo.

"""Q3
There are 155 banks involved in certain international transactions. A federal agency claims that 
at least 35% of these banks have total assets of over $10 billion (In U.S. dollars). An independent agency wants to 
test this claim. It gets a random sample of 50 out of the 155 banks and finds that 15 of them have total 
assets of over $10 billion. Can the claim be rejected?
"""
#Test about a population proportion p using a z-statistic. remember mu = p and var = p(1-p) since it's a 

"""Q4
General Motors Corporation hopes to reduce anticipated production costs of its Saturn Model by 
instituting an assembly schedule that will reduce average production time to about 40 hours per car. 
In a test run of the new assembly line, 40 cars are built at a sample average time per car of 46.5 hours 
and a sample standard deviation of 8.0 hours. A test run of 38 cars using the old assembly schedule results 
in a sample of mean of 51.2 hours and a sample deviation of 9.5 hours. Is there proof that the new assembly 
schedule reduces the average production time per car? What is the p-value? Explain.

why use pooled std?
https://onlinecourses.science.psu.edu/stat500/node/50/
"""
mu1, mu2 = 46.5, 51.2
std1, std2 = 8, 9.5
n1, n2 = 40, 38
df = n1+n2-2
def pool_std(std1,std2, n1, n2):
  return np.sqrt(((n1 - 1)*std1**2 + (n2 - 2)*std2**2)/(n1+n2-2))

pool_std1 = pool_std(std1,std2,n1,n2) #8.69

t_stats = (mu1 - mu2 - 0)/(pool_std1*np.sqrt(1/n1+1/n2))  # -2.386
p_value = st.t.cdf(t_stats, df = 76) # 0.0097


"""Q5
A telephone company wants to estimate the average length of long-distance calls during weekends. 
A random sample of 50 calls gives a mean |(\bar{X} =14.5\) min and standard deviation s = 5.6 min. 
Give a 95% confidence interval for the average length of a long-distance phone call during weekends.
"""
alpha = 0.05
n = 50
mu = 14.5
std = 5.6
z_value = st.norm.cdf(1 - alpha)

CI_upper = mu + z_value * std/np.sqrt(n)
CI_lower = mu - z_value * std/np.sqrt(n)


"""Q6
Several companies have been developing electronic guidance systems for cars. Motorola and Germany's 
Blauounkt are two firms in the forefront of such research. Out of 120 trials of the Motorola model, 
101 were successful; and out of 200 tests of the Blaupunkt model, 110 were successful. 
Is there evidence to conclude that the Motorola electronic guidance system is superior to the German competitor?
"""
# H0: p1 <= p2
p1 = 101/120
p2 = 110/200
n1,n2 = 120,200
mu = p1 - p2
std = np.sqrt(p1*(1-p1)/np.sqrt(n1) + p2*(1-p2)/np.sqrt(n2))

z_score = mu/std
p_value  = 1 -  st.norm.cdf(z_score) # p-value = 0.045
#since p_value is less than 0.05, so we conclude to reject null hypo























