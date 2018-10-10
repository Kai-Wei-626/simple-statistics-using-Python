"""
Questions and answers 1 - 6 are in the previous python file
https://onlinecourses.science.psu.edu/stat500/node/69/
"""
"""Q6
An important measure of the risk associated with a stock is the standard deviation, or variance, of the stock's price movements. 
A financial analyst wants to test the one-tailed hypothesis that stock A has a greater risk (larger variance of price) than stock B.
A random sample of 25 daily prices of stock A gives s2A=6.52, and a random sample of 22 daily prices of stock B gives 
a sample variance of s2B=3.47. Carry out the test at α=0.01.
"""
import scipy.stats as st
n1, n2 = 25, 22
var1, var2 = 6.52, 3.47
F = var1/var2 
df1 = n1 - 1 
df2 = n2 - 1

p_value = 1 - st.f.cdf(F, df1, df2) # 0.075
# p > 0.01 so reject null hypo



"""Q7
Analysis of variance has long been used in providing evidence of the effectiveness of pharmaceutical drugs. 
Such evidence is required before the FDA will allow a drug to be marketed. In a recent test of the
effectiveness of a new sleeping pill, three groups of 25 patients each were given the following treatments. 
One group was given the drug, the second group was given a placebo, and the third group was given no treatment at all.
The results are as follows.
Drug group	12, 17, 34, 11, 5, 42, 18, 27, 2, 37, 50, 32, 12, 27, 21, 10, 4, 33, 63, 22, 41, 19, 28, 29, 8
Placebo group	44, 32, 28, 30, 22, 12, 3, 12, 42, 13, 27, 54, 56, 32, 37, 28, 22, 22, 24, 9, 20, 4, 13, 42, 67
No-treatment group	32, 33, 21, 12, 15, 14, 55, 67, 72, 1, 44, 60, 36, 38, 49, 66, 89, 63, 23, 6, 9, 56, 58, 39, 59
Use a computer to determine whether or not the drug is effective.
What about the placebo? Give differences in average effectiveness, if any exist.
"""
# this is a classical question that can use one way ANOVA 
# let's draw a boxplot
l = [12, 17, 34, 11, 5, 42, 18, 27, 2, 37, 50, 32, 12, 27, 21, 10, 4, 33, 63, 22, 41, 19, 28, 29, 8]
l2 = [44, 32, 28, 30, 22, 12, 3, 12, 42, 13, 27, 54, 56, 32, 37, 28, 22, 22, 24, 9, 20, 4, 13, 42, 67]
l3 = [32, 33, 21, 12, 15, 14, 55, 67, 72, 1, 44, 60, 36, 38, 49, 66, 89, 63, 23, 6, 9, 56, 58, 39, 59]
x = ['drug'] * 25
x2 = ['placebo'] * 25
x3 = ['None'] * 25
l.extend(l2)
l.extend(l3)
x.extend(x2)
x.extend(x3)

import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({'group': x, 'value': l})
df.boxplot('value', by = 'group', figsize = (12,8))
F, p = stats.f_oneway(l, l1, l2) # p = 0.327

# p is large, we can conclude to reject null hypothesis under alpha level of confidence. We conclude meds is effective. but 
# will this gives us a conclusion that drug is different than placebo?  


"""Q8
The maker of portable exercise equipment, designed for the health-conscious people who travel too frequently 
to use a regular athletic club, wants to estimate the proportion of traveling business people who may be interested
in the product. A random sample of 120 traveling business people indicates that 28 of them may be interested 
in purchasing the portable fitness equipment. Give a 95% confidence interval for the proportion of all traveling
business people who may be interested in the product.
"""
p = 28/120
mu = p
var = p*(1-p)
se = np.sqrt(var/n)
z_stats = 1.96

CI_upper = mu + se*z_stats
CI_lower = mu - se*z_stats


"""
When new paperback novels are promoted at bookstores, a display is often arranged with copies of
the same book with differently colored covers. A publishing house wanted to find out whether there 
is a dependence between the place where the book is sold and the color of its cover. For one of 
its latest novels, the publisher sent displays and a supply of copies of the novels to large bookstores 
in five major cities. The resulting sales of the novel for each city-color combination are as follows.
Numbers are in thousands of copies sold over a three-month period.
	
          Color   Red  Blue  Green  Yellow  Total
City
      New York	  21	  27   	40	   15	     103
      Washington	14	  18  	28  	  8	      68
      Boston	    11	  13	  21    	7     	52
      Chicago   	3	    33   	30    	9     	75
      Los Angeles	30	  11	  34	    10	    84
      Total     	79	  102	  153	    49    	383
      
1. Assume that the data are random samples for each particular color-city combination and that 
the inference may apply to all novels. Conduct the overall test for independence of color and location.
2. Before the analysis, the publisher stated a special interest in the issue of whether there is any dependence
between the red versus blue preference and the two cities Chicago versus Los Angeles. Conduct the test. Explain.






















