"""
- Ranges ->
 - Precisamos conhecer o Loop for para usar os ranges.
 - Precisamos conhecer o range para trabalhar melhor com loops for

 Ranges são utilizaos parar gerar sequencias numericas, nnão de forma aleatoria,
 mas sim de maneira especifica.

 range(valor_de_parada) #valor em que vai -1 ou seja se for 11 o resultado de range sera 10

obs: (valor_de_parada) não inclusive (inicio padrao 0, e passa de 1 em 1 -1)
 obs
exemplo:
for num in range(11):
    print(num)

Exemplo 2

range(valor_de_inicio, valor_de_parada)
for num in range(1,11):
    print(num)

Exemplo 3 em passadas
for num in range(1, 10, 2): #esse 2 serve para definir de quantos em quantos numero ele vai "pular"
    print(num)

Exemplo 4 -igual a forma 3 porem inversa
range(valor_inicial, valor_de_parada, passo)
for num in range(10, -1, -1) #vai ser uma contagem regressiva
    print(num)

"""

