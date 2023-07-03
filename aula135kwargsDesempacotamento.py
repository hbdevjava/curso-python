# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'hebert',
    'sobrenome': 'brito',
}
print(pessoa)
print()

dados_pessoa = {
    'idade': 41,
    'altura': 1.80,
    'peso': 87.100,
}

print(dados_pessoa)
print()

# extrai tudo de pessoa para pessoa_completa
pessoa_completa = {**pessoa, **dados_pessoa,
                   'cor': 'pardo', 'nome': 'Alisson', 'peso': 86}
print(pessoa_completa)

for chave, valor in pessoa_completa.items():
    print(chave, valor)


print('    **KWARGS =  ', 'EMPACOTANDO ARGUMENTOS EM KWARGS')


def mostra_args_nomeados(*args, **kwargs):
    print('NOMEADOS = ', args)
    for chave, valor in kwargs.items():
        print(chave, valor)


mostra_args_nomeados(a, b, nome='hebert', idade=33)
print()

print('    **KWARGS =  ', 'DESEMPACOTANDO ARGUMENTOS EM KWARGS')
mostra_args_nomeados(**pessoa_completa)

# a, b = pessoa.items()
# a, b = pessoa
# a, b = pessoa.values()
# a, b = pessoa.keys()
# a, b = pessoa.values()
# b = pessoa
# (a1, a2), b = pessoa.items()
# print(a1, a2)
# print(b)
# print()

# for chave, valor in pessoa.items():
#     print(chave, valor)
