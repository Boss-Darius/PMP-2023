

import pymc

'''1)'''

with pymc.Model() as model:
    n=pymc.Poisson('n',10)
    Ylist=[0,5,10]
    TetaList=[0.2,0.5]

    for teta in TetaList:
        for y in Ylist:
            Y=pymc.Binomial('y',n,teta)

            data=pymc.sample(100,return_inferencedata=True)
            pymc.sample_posterior_predictive(data,model=model,extend_inferencedata=True)

