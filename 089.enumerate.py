"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# nomes = 'Maria', 'Helena', 'Luiz'
print()
# Casting => transforma um tipo noutro
# lista_enumerada = list(enumerate(nomes))

# lista_enumerada = list(nomes)
# print(lista_enumerada)
lista = 'Maria', 'Helena', 'Luiz'

for i, nome in enumerate(lista):
    print(i, nome)
print('aqui')

veriavel_enumerada = enumerate(lista)
print(next(veriavel_enumerada))

print()
# ENUMERA EXPLICITAMENTE:
for i, nome in enumerate(lista):
    print(i, nome)

print()
print('-='*30)
print()

for item in enumerate(lista):
    i, nome = item
    print(i, nome)

print()
print('-='*30)
print()

i = 0                       # SEM O ENUMERATE
for nome in lista:
    print(i, '=', nome)
    i += 1

print()


'''for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}'''
