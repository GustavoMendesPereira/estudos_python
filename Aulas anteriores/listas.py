"""
Listas

Listas em python funcionam como vetores, matrizes, com a diferença de serem dinamicos e tambem 
de podermos colocar QUALQUER tipo de dado.

- Dinamico:
"""
frutas = ["maça", "banana", "pera", "Abacaxi"]
"""print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
"""
"""
Metodo pra puxar a lista de modo invenso
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])
print(frutas[0])
"""
"""
frutas.append("Jabuticaba")
frutas.insert(1,"melancia")
print(frutas)
frutas.remove('banana')
print(frutas)
fruta_removida = frutas.pop(3)
print(fruta_removida)
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)
"""
números = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  