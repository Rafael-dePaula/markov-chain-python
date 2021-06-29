# Markov-Chain
## Definições
__Suposição de Markov__ diz que desde que o estado atual seja conhecido os estados anteriores são irrelevantes para calcular o proximo estado.

A __Cadeia de Markov__ é um processo estocástico onde dada uma sequencia de estados X1, X2, X3, ... de variáveis aleatórias, a probabilidade do estado Xn+1 pode ser calculada apenas baseada no estado Xn.

   <img src="https://user-images.githubusercontent.com/78245128/123849098-cee71980-d8ee-11eb-91ba-1b5205a06664.png" align="cente" border="0" alt="P(X_{n+1} = x | X_0, X_1, X_2 ... X_n) = P(X_{n+1} = x|X_n)" width="364" height="18" />

Ou seja para calcular um determinado estado Xn+1 na cadeia de markov basta que tenhamos o estado anterior (Xn) conhecido e conhecer as probabilidades de transição entre os estados dessa cadeia.


 ## Exemplo Sol e Chuva
 > Para o codigo desse exemplo foi usada a biblioteca pomegranate

 Para o exemplo Sol e Chuva temos que a probabilidade de um dia de sol ser sucedido por um dia chuva é de 10% e a probabilidade de um dia de chuva ser sucedido por um dia de sol é de 60%.

Com essas probabilidades é possivel definir o modelo de transição entre os estados:

__Modelo de Transição__
|          |      Sol      | Chuva |
|:----------|:-------------:|:------:|
| __Sol__  |  0.9          | 0.1   |
| __Chuva__|  0.6          | 0.4   | 

<img src="https://user-images.githubusercontent.com/78245128/123842166-dc98a100-d8e6-11eb-82ae-1d4a761423e4.png" width="330">

Que no codigo é definido como:
```python
modeloTransicao = ConditionalProbabilityTable([['sol', 'sol', 0.9],
                                      ['sol', 'chuva', 0.1],
                                      ['chuva', 'sol', 0.6],
                                      ['chuva', 'chuva', 0.4]], [estadoInicial])
```
Com essas possibilidades basta definir o __Estado Inicial__, que será o primeiro valor da cadeia.
No codigo foi usado 50% de chance de ser sol e 50% de ser chuva.
```python
estadoInicial = DiscreteDistribution({'sol': 0.5, 'chuva': 0.5})
```
| Sol | Chuva|
|:------:|:------:|
| 0.5 |  0.5 |

Com essas informações é possivel criar uma __cadeia de markov__.
```python
model = MarkovChain([d1, d2])
```
__Amostra__

Para criar uma amostra basta usar o metodo ```sample()``` e passar como parametro o tamanho da cadeia que deseja gerar.


```python
model.sample(10)
```
Por exemplo com 10 amostras uma das possiveis cadeias geradas é:

| Sol | Chuva | Chuva | Sol | Sol | Sol | Sol | Sol | Chuva | Sol |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
  
