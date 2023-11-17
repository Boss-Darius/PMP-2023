from google.colab import files

import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import numpy as np
import numbers

uploaded = files.upload()

'''1)'''
# Incarcam setul de date
df = pd.read_csv('auto-mpg.csv')

# Curatam datele (daca este necesar)
# De exemplu, eliminam valorile lipsa
df = df.dropna()

# Trasam graficul
plt.scatter(df['horsepower'], df['mpg'])
plt.xlabel('Cai putere (CP)')
plt.ylabel('Mile per galon (mpg)')
plt.title('Relația dintre CP și mpg')
plt.show()
'''2)'''

horsenp = df['horsepower']
horsenp = horsenp.drop(['34', '128', '332', '338', '356', '376'])

print("len-nr=", len(horsenp) - nr)
# Definim modelul
with pm.Model() as model:
    # Coeficienti pentru intercept si CP
    alpha = pm.Normal('alpha', mu=0, sigma=10)
    beta = pm.Normal('beta', mu=0, sigma=10)

    # Modelul liniar
    mu = alpha + beta * horsenp

    # Precizia (inversa a variantei)
    sigma = pm.HalfNormal('sigma', sigma=1)

    # Definim distributia normala a mpg
    mpg = pm.Normal('mpg', mu=mu, sigma=sigma, observed=df['mpg'])
'''c)'''
with model:
    # Folosim MCMC pentru a estima parametrii
    trace = pm.sample(1000, tune=1000)

# Sumarul rezultatelor
pm.summary(trace, var_names=['alpha', 'beta', 'sigma'])

# Trasam dreapta de regresie
plt.scatter(df['horsepower'], df['mpg'])
plt.xlabel('Cai putere (CP)')
plt.ylabel('Mile per galon (mpg)')

# Trasam dreapta de regresie medie
x_vals = np.linspace(df['CP'].min(), df['CP'].max(), 100)
y_vals = trace['alpha'].mean() + trace['beta'].mean() * x_vals
plt.plot(x_vals, y_vals, 'r-', label='Dreapta de regresie medie')

plt.legend()
plt.show()

'''d)'''
plt.scatter(df['horsepower'], df['mpg'])
plt.xlabel('Cai putere (CP)')
plt.ylabel('Mile per galon (mpg)')

# Trasam dreapta de regresie medie
plt.plot(x_vals, y_vals, 'r-', label='Dreapta de regresie medie')

# Adaugam regiunea 95% HDI
pm.plot_posterior_predictive_glm(trace, samples=100, eval=np.linspace(df['CP'].min(), df['CP'].max(), 100),
                                 label='Regiune 95% HDI')

plt.legend()
plt.show()