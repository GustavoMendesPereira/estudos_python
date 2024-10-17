"""
Recebendo dados do usuario

print("qual seu nome")
nome = input() #input significa entrada

# Metodo antigo 2.x
print('seja bem vindo(a) %s' % nome)

print("Qual a sua idade?")
idade = input()

#processamento

# Saida de dados

# Metodo antigo 2.x
print('O(a) %s tem %s anos' % (nome, idade)) # o primeiro %s vai substituir o valor do 1 em parentese 
# e assim sucetivamente
"""

# Modelo moderno de se utilizar 
#print("Qual seu nome?")
nome = input('Qual o seu nome?')

# Metodo atual 3.x
# print('Seja bem-vindo(a) `{0}' .format(nome))


#Forma mais moderna de se fazer
print(f'seja bem vindo(a){nome}')

#print("Qual sua idade?")
idade = int(input('Qual a sua idade?'))

# Metodo atual 3.x
# print('A {0} tem {1} anos' .format(nome, idade))

#Forma mais moderna de se fazer.
print(f'A {nome} tem {idade}')


#int-idade -> Cast
#cast e um tipo de 'conversão' de um tipo de dado para outro ou seja aqui esta passando de uma string para 
# um numero inteiro
print(f'A{nome} nasceu em `{2024 - idade}')
# Aspas Duplas triplas -> """Gustavo"""


# O texto para fazer as perguntas pode ser passado diretamente no input por exemplo:
# nome = input('Qual o seu nome')
# O mesmo serve para a idade
# idade = input('qual a sua idade)