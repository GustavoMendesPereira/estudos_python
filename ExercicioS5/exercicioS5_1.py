"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.
"""
contador: int = 0
indice: int = 1

while contador < 5: #enquanto o contador for menor que 5 ele vai continuar puxando o codigo
    if indice % 3 == 0:   #se o valor de indice for divisivel por 3 e for igual a 0 ele vai continuar executando o codigo
        print(f'o numero {indice} e multiplo de 3. ')
        contador = contador + 1 #serve para continuar executando o codigo ate chegar em 5
    indice = indice + 1 # vai somando 1 em 1 ate chegar num valor divisivel por 3 