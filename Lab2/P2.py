import numpy as np
import matplotlib.pyplot as plt
import random
import arviz as az
import scipy.stats

from scipy.stats import expon

s1=scipy.stats.gamma(4,3).rvs()
s2=scipy.stats.gamma(4,2).rvs()
s3=scipy.stats.gamma(5,2).rvs()
s4=scipy.stats.gamma(5,3).rvs()

number=np.random.random()

if number <0.2 :
    x=s4
elif number >0.2 and number <0.45:
    x=s1
elif number >0.45 and number<0.7:
    x=s2
else:
    x=s3

az.plot_kde(x)
plt.show()

print(expon.cdf(x,3,4))

