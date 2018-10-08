"""
Analysis of Variance
The one-way ANOVA tests the null hypothesis that two or more groups have the same population mean. 
The test is applied to samples from two or more groups, possibly with differing sizes.

The ANOVA test has important assumptions that must be satisfied in order for the associated p-value to be valid.

1. The samples are independent.
2. Each sample is from a normally distributed population.
3. The population standard deviations of the groups are all equal. This property is known as homoscedasticity.
If these assumptions are not true for a given set of data, it may still be possible to use the Kruskal-Wallis H-test (scipy.stats.kruskal) although with some loss of power.

(https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html)


SST(total variance)
SSW(within group)
SSB(between group)

The dataset we are using is from here:
https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
"""
from scipy import stats

datafile = "PlantGrowth.csv"
data = pd.read_csv(datafile)
 
#Create a boxplot
data.boxplot('weight', by='group', figsize=(12, 8))
 
ctrl = data['weight'][data.group == 'ctrl']
 
grps = pd.unique(data.group.values)
d_data = {grp:data['weight'][data.group == grp] for grp in grps}

# degree of freedom 
k = len(pd.unique(data.group))  # number of conditions
N = len(data.values)  # conditions times participants
n = data.groupby('group').size()[0] #Participants in each condition
 
F, p = stats.f_oneway(d_data['ctrl'], d_data['trt1'], d_data['trt2'])
