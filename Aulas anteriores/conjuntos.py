"""
Para criar um conjunto, utilize chaves ou a função set():
"""
frutas = {"maça", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

#Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2 #junta meus 2 conjuntos
print(uniao)

intersecao = conjunto1 & conjunto2  # numeros que possue nos dois conjuntos
print(intersecao)

diferenca = conjunto1 - conjunto2 # Mostra que elementos estão no conjunto 1 e não no 2
print(diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2 # mostra somente os numeros diferentes nos 2 conjuntos
print(diferenca_simetrica)


frutas = {"maçã", "banana", "laranja"}

frutas.add("pera") #adiciona a fruta pera
print(frutas)  

frutas.remove("banana") #remove a fruta banana
print(frutas)  

frutas.discard("uva") #discarta a uva
print(frutas)  

frutas.clear() # retorna set()
print(frutas)  