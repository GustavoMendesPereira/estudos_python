"""
Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. 
Este arquivo pode estar vazio ou conter código de inicialização do pacote.
Por exemplo, criamos um diretório chamado meu_pacote com a seguinte estrutura:
"""
meu_pacote/ 
    __init__.py
    modulo1.py
    modulo2.py


from meu_pacote import modulo1, modulo2


modulo1.funcao1()
modulo2.funcao2()