"""
Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, 
como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.
"""
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

"""
Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). 
Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.
"""
arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()