"""
Tipo float numero flutuando com casas decimais


Tipo real, decimal

Casas decimais

OBS: O separador de casas decimais na programação e o ponto e não a virgula
"""

# Errado no ponto de vista do FLOAT mas gera uma tupla

#valor = 1, 44

# Certo no ponto de vista do FLOAT
valor = 1.44

# Podemos fazer
valor1, valor2 = 1, 44

print(valor)

print(valor1)
print(valor2)

# Podemos converter um FLOAT para um INT
resultado = int(valor) # Quando colocamos em INT perdemos precisão do resultado
print(resultado)