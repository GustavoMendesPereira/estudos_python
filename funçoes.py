"""
Para definir uma função em Python, utilizamos a palavra-chave def seguida do nome da função e parênteses. 
Opcionalmente, podemos especificar parâmetros dentro dos parênteses. 
O bloco de código da função é indentado após os dois pontos.
Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses:
"""
"""
def saudação ():
    print("Olá, mundo!")

saudação()
"""
"""
def saudacao(nome): #nome serve como um parametro para chamar no meu print
    print(f"Olá, {nome}!")
saudacao('Gustavo')
saudacao('Maria') #aqui definimos o que esta dentro do parametro da minha função

def soma(a,b):
    return a + b
resultado = soma(4,9)
print(f'a soma e:{resultado}')

#Funçoes anonimas, chamadas de funções lambdas
# permitem que crie uma função sem nome de definição usadas em funções pequenas e consiças 
quadrado = lambda x: x ** 2
print(quadrado(7)) # definimos o nosso parametro ja no final da função 
"""
def funcao():
    variavel_local = 10
    print(variavel_local) 
funcao()


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20

"""
É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto 
que descrevem o propósito, os parâmetros e o valor de retorno de uma função. 
São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.
"""
def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura


def soma_variavel(*numeros): #utilizando o * antes da variavel podemos utilizar um numero variavel
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(22, 22, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22