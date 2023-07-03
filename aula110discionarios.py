# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
print('-=-=-=-=-=-=-=- EX 1 -=-=-=-=-=-=-=-=-')
# VALOR DA CHAVE É IMUTAVEL
familia = {
    'pai_1': 'Hebert',
    'familia_hb': [
        {'pai': 'Brito',
         'mae': 'Fabia',
         'irmaos': [
             {'irma': 'Janainna',
              'irmao_1': 'joao',
              'irmao_2': 'hyago',
              'sobrinhos': [
                  {'sobrinha_1': 'leticia', 'filha': 'Janainna',
                   'sobrinho_2': 'davi', 'filho': 'joao',
                   'sobrinha_3': 'livia', 'filho': 'joao',
                   'sobrinho_4': 'marcos', 'filho': 'hyago'

                   },
              ],

              },

         ],
         },

    ],
    'pai_2': 'Alisson',
    'filha': 'Dorinha',
}
print('{:=^100}'.format(' ACESSSAR: CHAVES, VALORES DENTRO DO DICIONARIOS '))
print()
print(familia.values())
print()
print(familia.keys())
print()
print(familia.items())
print()

print('{:=^100}'.format(' ACESSSAR: ESPECIFICAMENTE O OBJ DESEJADO'))
print()
for i, nome in enumerate(familia):
    print(i, '=', nome)

print(list(familia.keys()))

# print(familia['familia_hb'])
print()


print('-=-=-=-=-=-=-=- EX 2 -=-=-=-=-=-=-=-=-')

familia = dict(pai_1='hebert',
               pai_2='Alisson',
               filha='Dorinha')

print(familia)

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)
