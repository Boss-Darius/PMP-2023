# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import random
import numpy as np
from scipy import stats

'''1)'''
numar=300
Clienti=stats.poisson(20)

NrClienti=Clienti.rvs(size=numar)
print(NrClienti)

T=[]
G=[]
Gatire=stats.expon(1/15)
Timp=stats.norm(2,0.5)

for i in range(0,numar):
    Ti=[]
    Gi=[]
    for j in range(0,NrClienti[i]):
        Ti+=[Timp.rvs()]
        Gi+=[Gatire.rvs()]
    T+=[Ti]
    G+=[Gi]

#print("T=",T)
#print("G=",G)

'''2'''

probabilitate=0
#
NrClienti=Clienti.rvs(size=100000)
#
l=0.01
while probabilitate<0.95:
    Gatire=stats.expon(1/l)
    for i in range(0, 100000):
        Ti = []
        Gi = []
        for j in range(0, NrClienti[i]):
            Ti += [Timp.rvs()]
            Gi += [Gatire.rvs()]
        T += [Ti]
        G += [Gi]
        sum=0
        for i in range(0,len(T)):
            for j in range(0,len(T[i])):
                if T[i][j]+G[i][j]< 15:
                    sum+=T[i][j]+G[i][j]

    probabilitate=sum/100000
    l=l+0.01
'''in mod normal as adauga la l un numar mic(de exemplu 0.001), dar programul va rula mult mai mult'''
print(l)

'''3) consideram lamda=0.09'''

Clienti=stats.poisson(20)

NrClienti=Clienti.rvs(size=10)

Gatire=stats.expon(1/0.09)
Timp=stats.norm(2,0.5)

for i in range(0,10):
    sum=0
    for j in range(0,NrClienti[i]):
        sum=sum+Timp.rvs()+Gatire.rvs()
    print('Timpul mediu de servire pentru client este: ', sum/NrClienti[i])











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
