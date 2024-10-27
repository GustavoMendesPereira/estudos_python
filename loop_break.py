"""
Saindo de loop com break

Utilizamos o break para sair de loops de maneira projetada.

"""
#exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('sai do loop')

while True:
    comando = input("Digite sair para sair: ")
    if comando == 'sair':
        break