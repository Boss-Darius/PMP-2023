
''''''

''''''

import pymc3 as pm
import numpy as np
'''1)'''
data=np.loadtxt("trafic.csv")
dataSize=len(data)

with pm.Model() as model:

    lambda1=pm.Exponential("Alpha1",1/dataSize)
    lambda2 = pm.Exponential("Alpha2", 1 / dataSize)
    lambda3 = pm.Exponential("Alpha3", 1 / dataSize)
    lambda4 = pm.Exponential("Alpha4", 1 / dataSize)
    lambda5 = pm.Exponential("Alpha5", 1 / dataSize)

    tau1=pm.DiscreteUniform("tau1",lower=0,upper=dataSize-1)
    tau2=pm.DiscreteUniform("tau2", lower=0, upper=dataSize - 1)
    tau3=pm.DiscreteUniform("tau3",lower=0,upper=dataSize-1)
    tau4=pm.DiscreteUniform("tau4",lower=0,upper=dataSize-1)

    index=np.arange(dataSize)
    parameter=pm.math.switch(tau1>index,lambda1,lambda2)
    parameter=pm.math.switch(tau2>index,lambda2,lambda3)
    parameter=pm.math.switch(tau3>index,lambda3,lambda4)
    parameter=pm.math.switch(tau4>index,lambda4,lambda5)

    generator=pm.Poisson("Valori de trafic",parameter,observed=data)

'''2)'''

Hmap=pm.find_MAP(model=model)