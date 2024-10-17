"""
Tipo String

Ja vimos que em python um dado e considerado do tipo String, sempre que estiver em aspas simples.
por exemplo: 'uma string', '1234', 'a', 'True'
Sempre que estiver em aspas duplas: "uma String", "1234", "a", "True"
Sempre que estiver em aspas simples triplas:  '''uma String''', '''1234''', '''a''', '''True'''
# sempre que estiver em aspas duplas triplas :"""#uma String""", """1234""", """a""", """a"""


"""
nome = 'Gustavo Mendes' #Utilização de aspas simples normal
print(nome)

nome = "Gina's Bar" #aspas duplas utilizada quando for utilizar um nome com aspas simples
print(nome)

nome = 'Gustavo \nmendes' #\n utilizado para descer a string em seguida para a linha de baixo
print(nome)

nome= """#Gustavo"""
# Mendes"""  # Mesma função do \n porem mais simples, utilizando apenas aspas duplas triplas
# print(nome)

# Sempre fechar as aspas com a aspas que foi aberta idependente de qual for
# Caso queira utilizar uma aspas igual a de abertura dentro das aspas utilizar \ e a aspás que deseja utilizar

# nome = 'Gustavo \' mendes'
#print(nome)

# print(nome.upper) Coloca todas as letras da variavel em caixa alta
# print(nome.lower) Coloca todas as letras da variavel em letras minuscula
# print(nome.split) Transforma todas as strings separadas por espaço em listas


"""
"""
#  0,   1,   2,   3,   4,   5,   6
#['G', 'u', 's', 't', 'a', 'v', 'o']
nome = 'Gustavo'
print(nome[2:7]) # Isso se chama Sclice String utilizar [] para definir ate onde quer 

#Caso queira invertir a string do ultimo ate o primeiro utilize [::-1] Começe do primeiro elemento, va ate o ultimo elemento e inverta
print(nome[::-1]) #Metodo pythonico de reversão ja que não podemos utilizar o reverse

print(nome.replace('o', 'j')) #troca a letra na primeira aspas pela segunda
