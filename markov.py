from pomegranate import *
estadoInicial = DiscreteDistribution({'sol': 0.5, 'chuva': 0.5})
modeloTransicao = ConditionalProbabilityTable([['sol', 'sol', 0.9],
                                      ['sol', 'chuva', 0.1],
                                      ['chuva', 'sol', 0.6],
                                      ['chuva', 'chuva', 0.4]], [estadoInicial])

model = MarkovChain([estadoInicial, modeloTransicao])

for amostra in model.sample(100):
    print (amostra)
