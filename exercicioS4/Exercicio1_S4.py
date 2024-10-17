"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""
numero1: int = int(input("Qual o primeiro numero:"))
numero2: int = int(input("Qual o Segundo numero:"))

if numero1 > numero2:
    print("Numero 1 e maior")
elif numero1 == numero2:
    print("Os numeros são iguais!")
else:
    print("numero 2 e maior")