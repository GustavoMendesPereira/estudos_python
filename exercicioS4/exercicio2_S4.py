"""
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""
numero1: int = int(input('Digite um numero:'))

if numero1 >= 0:
    print(f'A raiz quadrada do seu numero e:{numero1 ** numero1}' )
else:
    print(f'O seu numero:{numero1} e invalido')