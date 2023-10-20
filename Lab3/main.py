

'''C independenta'''
'''I dependenta de C'''
'''A dependenta de C si I'''

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx

model=BayesianNetwork([('C','I'),('I','A'),('C','A')])

CPD_Cutremur=TabularCPD(variable='C', variable_card=2,values=[[0.0005],[0.9995]])

CPD_Incendiu=TabularCPD(variable='I',variable_card=2,values=[
                                                             [0.99,0.97],
                                                             [0.01,0.03]],
                        evidence=['C'],evidence_card=[2])

CPD_Alarma=TabularCPD(variable='A',variable_card=2,values=[
                                                           [0.99999,0.98,0.05,0.02],
                                                            [0.0001,0.02,0.95,0.98]
                                                            ],
                      evidence=['C','I'],evidence_card=[2,2])

model.add_cpds(CPD_Alarma,CPD_Incendiu,CPD_Cutremur)

assert model.check_model()
print('Probabilitatea ca un cuntremur sa fi avut loc, stiind ca s-a activat alarma')
'''C(1)'''
infer = VariableElimination(model)
result = infer.query(variables=['C'], evidence={'A': 1})
print(result)

print('Probabilitatea ca un incendiu sa fi avut loc, stiind ca alarma nu s-a activat')
'''I(1)'''
infer = VariableElimination(model)
result = infer.query(variables=['I'], evidence={'A': 0})
print(result)

pos = nx.circular_layout(model)
nx.draw(model, pos=pos, with_labels=True, node_size=4000, font_weight='bold', node_color='skyblue')
plt.show()