"""
Ao contrário das listas, as tuplas são imutáveis, o que significa que não podem ser modificadas uma vez criadas.
Não se pode adicionar, eliminar ou alterar elementos em uma tupla existente.
As tuplas são úteis quando você precisa armazenar uma coleção de elementos que não devem ser modificados, 
como coordenadas ou dados de configuração.
"""
ponto = (3,4)
print(ponto[0])
print(ponto[1])

minha_tupla = (1, 2, 3, 2, 4, 2)

print (minha_tupla.index(2)) 
print (minha_tupla.index(2, 2))  
print (minha_tupla.index(2, 2, 4)) #basicamente define quantos ele vai pular
#exemplo 2,2,4 pula 
