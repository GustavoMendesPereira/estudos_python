"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar
"""
numero: int = int(input('Digite um numero:'))

if numero % 2 == 0:
    print(f'O numero {numero} e par!')
else:
    print(f'O numero {numero} e impar!')