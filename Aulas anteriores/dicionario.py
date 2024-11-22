pessoa = {"nome":"Gustavo", "idade":25, "cidade": "Brasilia DF"}
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa.update({"profissão": "programador"})
print(pessoa)