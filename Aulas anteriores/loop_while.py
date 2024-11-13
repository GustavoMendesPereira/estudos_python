"""
- While

forma geral

Pode ser usado como um loop infinito

While expressão_booleana:
    //execução do loop

O bloco do while sera repetido enquanto a expressão booleana for verdadeira

expressão booleana e toda expressão onde o resultado é verdadeiro ou falso,

exemplo:

num = 5
num < 5

numero = 1

while numero < 10:
    print(numero)
    #numero = numero + 1


# em um loop while e importante que cuidemos do criterio de parada.
"""
resposta = ' '
while resposta != 'não':
    resposta = input('no ceu tem pão? ')
if resposta == 'não':
    print('e morreu')