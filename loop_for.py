"""
loop for 
O loop e uma estrutura de repetição  
for e uma parte disso

Em python utilizamos assim
for item in interavel:
    //execução do looping

Utilizamos o loop para sequencia ou valores iteraveis
Exemplo de valores iteraveis:
-> Strings
    Nome = 'Gustavo Mendes'
-> Lista
    lista = [1, 2, 3, 4, 5]
-> Range
    Numeros = [1, 10]

nome = 'Gustavo'
lista = [1, 2, 3, 74, 5, 6]
numeros = range(1, 10) #temos que transformar em lista

#exemplo de for 1 interando sobre String
for letra in nome:
    print(letra)

#exemplo de for 2 iterando sobre uma lista
for numero in lista:
    print(numero)

#exemplo de for 3 iterando sobre range

Em range utilizamos o valor Inicial e o valor Final
então quando colocamos o valor de 1-10 ele nos mostrara somente ate o 9
pois o valor final não e incluido
ou seja se eu quiser que va de 1-10 tenho que definir o valor de range para 1-11

for numero in range(1, 11):
    print(numero)    
   

#enumerate gera uma tupla da string de nome
for _, letra in enumerate(nome):
    print(letra) 
OBS: QUando não precisamos de um valor, podemos descarta-lo utilizando um underline(_)


for indice, letra in enumerate(nome):
    print(nome[indice])

    for indice, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

nome = 'Gustavo'
lista = [1, 2, 3, 74, 5, 6]
numeros = range(1, 10) #temos que transformar em lista

qtd = int(input('Quantas vezes o loop ira rodar?'))
soma = 0 #valor atribuido e 0 para fazer a soma dos numeros informados

#for n in range(1, qtd+1):
   # print(f'imprimindo{n}')

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}')
"""
nome = 'Gustavo'

for letra in nome:
    print(letra, end=' ') 
#Por padrao o python ja usa o \n  que separa por linhas as letras então para deixalar juntas usamos end=' '

variavel1 = 254
print(help(variavel1))