from pomegranate import *
d1 = DiscreteDistribution({'sol': 0.5, 'chuva': 0.5})
d2 = ConditionalProbabilityTable([['sol', 'sol', 0.9],
                                      ['sol', 'chuva', 0.1],
                                      ['chuva', 'sol', 0.6],
                                      ['chuva', 'chuva', 0.4]], [d1])

model = MarkovChain([d1, d2])

for valor in model.sample(100):
    print (valor)
