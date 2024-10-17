"""
Estruturas logicas: And(e), or (ou), NOT(não), IS(e)
    Operadores unarios:
    - NOT, 
    Operadores binarios:
    - AND, OR, IS

Para o AND, ambos os valores precisam ser True
Para o OR um ou outro valor precisa ser True
Para o NOT, o valor do Boleano e invertido ou seja se for True vira False e se for False vira True
"""
ativo = True
logado = False

if ativo and logado:
    print('Usuario ativo no sistema')
else:
    print('Voce precisa ativar sua conta, por facvor, cheque seu e-mail')