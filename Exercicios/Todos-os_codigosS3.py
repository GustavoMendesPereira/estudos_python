"""
1. Faça um programa que leia um número inteiro e imprima-o.
"""

numero: int = int(input('Qual o numero?'))

print(numero)

"""
2. Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.
"""

numero1: int = int(input("Digite seu primeiro numero:"))
numero2: int = int(input("Digite seu segundo numero:"))
numero3: int = int(input("Agora digite o terceiro numero:"))

resultado: int = numero1 + numero2 + numero3
print(f"A soma dos numero {numero1} com {numero2} e {numero3} e igual a {resultado}")

"""
3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
"""
valor1: int = int(input("Digite o primeiro valor:"))
valor2: int = int(input("Digite o segundo valor:"))
valor3: int = int(input("Agora digite o terceiro valor:"))

resultado: int = (valor1 * valor1) + (valor2 * valor2) + (valor3 * valor3)
print(f"A soma dos quadrados de {valor1} com {valor2} e {valor3} e igual a : {resultado}")
