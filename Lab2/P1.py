import statistics

import numpy as np
import matplotlib.pyplot as plt
import random
import arviz as az

time=0
p1=0.4
p2=0.6
X=np.ndarray([])
for i in range(0,10000):
    number = random.random()
    if number<p1:
        time=time+4
        X=np.append(X,number)
    else:
        time=time+6
        X=np.append(X,number)

print("Timpul mediu:")
print(time/10000)

print("Deviata medie:")
print(statistics.stdev(X))

az.plot_kde(X)

plt.show()