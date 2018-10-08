'''
Chi_square test

1. A test of goodness of fit establishes whether an observed frequency distribution differs from a theoretical distribution.
chi_square stats = summ[(observed frequency - theoretical frequency)^2/theoretical frequency]
chi_square stats follows chi square distribution
then use degree of freedom and significance level to look for the critical value in the chi-square chart

2. contingency table chi square test:
                      Med1      Med2      Placebo     total
#sick     Observed    20        30          30         80 (21%)
          expected    

#NotSick  Observed    100       110         90         300 (79%)
          expected
          
          total       120       140         120         380
calculate the expected number then caluculate the chi square stats
be awared of the degree of freedom is 2.
'''

# in the example above, we can use scipy function below
# scipy.stats.chisquare(f_obs, f_exp=None, ddof=0, axis=0)
from scipy.stats import chisquare

total = [120, 140, 120]
l1 = [i*0.21 for i in total]
l2 = [i*0.79 for i in total]
l1.extend(l2)
list_expect = l1
list_obs = [20, 30, 30, 100, 110, 90]

chisquare(list_obs, list_expect, ddof = 3)

## result:
#  Power_divergenceResult(statistic=2.5310715003300901, pvalue=0.28208812688912532)

the result indicates the chi-square stats is 2.53, and p-value is 0.282, we fail to reject the null hypothesis. The Meds has no effect

