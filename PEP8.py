"""
PEP8 - Python Enchancement Proposal 

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia de PEP8 que possamos escrever codigos em Python de forma Phytônica - Forma elegante

[1] - Utilize Camel Case para nomes de classes;
[2] - Utilize nomes em minusculo, separados por Underline(_) para funções ou variáveis;



class Calculadora:
    pass


class CalculadoraCientifica: #colocar letra maiuscula para cada começo de palavra pra não utilizar o _
    pass


def Soma():
    pass


def soma_dois():
    pass


numero = 4


numero_impar = 1



[3] - Utilize 4 espaços para identação (não usar TAB) apertar espaço 4x 
sempre depois de um bloco ou seja depois dos :




if 'a' in 'banana':
    print('tem')



[4] - Sempre utilizar 2 linhas em branco depois de uma classe
- Separar funçoes e definições de classe com duas linhas em branco;
- Metodos dentro de uma classe devem ser separados com uma unica linha em branco;



class Classe:
    pass


class Outra:
    pass



[5] Imports
- Imports devem ser sempre feitos em linhas separadas;




#errado
import sys, os


#import certo
import sys #Nestes 2 modelos estamos importandos os pacotes completos
import os

#não tem problema utilizar:

from types import StringType, ListType #importandoa apenas as classes StringType e a classe ListType


#Caso va fazer muitos imports de um mesmo pacote, utilize:
from types import(
    StringType,
    ListType,
    SetType,
    OutroType,    #Sempre utilizar a , depois do pacote que quer importar e sempre utilizar letra maiuscula 
)

# - Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentario ou DocString
# - Antes de constante ou variaveis globais. Sempre no topo do pragama nas Primeiras linhas

[6] - Espaços em expressões e instruções


# Não faça:
funcao( algo[ 1 ], { outro: 2} )

# Faça:
funcao(algo[1], {outro: 2})

# Não faça:
algo (1)

# Faça:
algo(1) # Parentese sempre junto

# Não faça:
dict ['chave'] = lista[indice]

#Faça:
dict['chave'] = lista[indice]

#Não Faça:
x              = 1
y              = 3
variavel_longa = 4

# Faça:
x = 1
y = 3
variavel_longa = 4

[7] - Termine sempre uma instrução com uma nova linha
"""
#deixar sempre uma linha em branco apos qualquer coisa que voce escrevera
print('Hellow World')