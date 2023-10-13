import numpy as np
import matplotlib.pyplot as plt
import random
import arviz as az

C1= np.array([])
C2=np.array([])
C3=np.array([])
C4=np.array([])

for i in range(0,1):
    ss = 0
    sb = 0
    bs = 0
    bb = 0
    for j in range(0,10):
        number1 = random.random()
        number2=random.random()

        if number1 < 0.3 and number2< 0.5 :
            ss=ss+1
        elif number1 > 0.3 and number2< 0.5:
            bs=bs+1
        elif number1 > 0.3 and number2> 0.5:
            sb=sb+1
        elif number1 < 0.3 and number2 > 0.5:
            bb=bb+1
        print(ss,' ',sb,' ',bs,' ',bb)
    C1=np.append(C1,ss/10)
    C2 = np.append(C2, sb / 10)
    C3 = np.append(C3, bs / 10)
    C4 = np.append(C4, bb / 10)

az.plot_kde(C1)
plt.show()
az.plot_kde(C2)
plt.show()
az.plot_kde(C3)
plt.show()
az.plot_kde(C4)
plt.show()
