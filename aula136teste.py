import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40,)


print('  COPIA USANDO LISTCOMPREHSITION')

numeros = ['hebert', 'alisson', 'dora', 'fabia', 'brito']

novo_numero = [
    nome for nome in numeros

]
print(novo_numero)
print()
print('  COPIA USANDO SHALLOWCOPY')

numeros = ['hebert', 'alisson', 'dora', 'fabia', 'brito']

novo_numero = numeros.copy()
print(numeros)
"""
# na shellow copy somente a copia é alterado a lista original permanece igual
['hebert', 'alisson', 'dora', 'fabia', 'brito']
['marcos', 'alisson', 'dora', 'fabia', 'brito'] 
    
"""
novo_numero[0] = 'marcos'
print(novo_numero)
print()
print('  COPIA USANDO FOR ')

numeros = ['hebert', 'alisson', 'dora', 'fabia', 'brito']

novo_numero = []
for pessoa in numeros:
    novo_numero.append(pessoa)

print(novo_numero)
print()

print('  AÇOES USANDO LISTCOMPREHSITION')

numeros = [12, 56, 31, 45, 12, 3]
mais = [num + 2 for num in numeros]
menos = [num - 2 for num in numeros]
multi = [num * 2 for num in numeros]
divid = [num / 2 for num in numeros]

print(numeros)
print(mais, 'soma + 2')
print(menos, 'diminui - 2')
print(multi, 'multiplica * 2')
print(divid, 'divide  / 2')
print()
"""
ELE EXECUTA TODAS ESSAS FUNCOES SEM AFETAR A LISTA ORIGINAL E ESSAS LISTAS SEMPRE TEM O MESMO TAMANHO
    
"""
print('    ENVOLVENDO EM FUNÇOES   ')


def adicinar(x, y):
    return x + y


def diminuir(x, y):
    return x - y


def multplicar(x, y):
    return x * y


def dividir(x, y):
    return x / y


numeros = [12, 56, 31, 45, 12, 3]
mais = [adicinar(num, 2) for num in numeros]
menos = [diminuir(num, 2) for num in numeros]
multi = [multplicar(num, 2) for num in numeros]
divid = [dividir(num, 2) for num in numeros]

print(numeros)
print(mais, 'soma + 2')
print(menos, 'diminui - 2')
print(multi, 'multiplica * 2')
print(divid, 'divide  / 2')
print()

print('     LISTA COMPREHESION FILTROS')

numeros = [1, 56, 78, 56, 41, 66, 32, 451, 63, 27]
numero_em_condicoes_1 = [num for num in numeros if num > 66]
numero_em_condicoes_2 = [num for num in numeros if num < 66]
numeros_impares = [num for num in numeros if num % 2 != 0]
numeros_pares = [num for num in numeros if num % 2 == 0]
outro_if = [
    num if num != 66 else 600 for num in numeros_pares
    # SE É ISSO O VALOR É ISSO SE NAO O VALOR É ISSO (OPEAÇAO TERNARIA)
]
print(numero_em_condicoes_1)
print(numero_em_condicoes_2)
print(numeros_impares, 'IMPARES')
print(numeros_pares, 'PARES')
print(outro_if, 'TROCOU 66 -> 600 ')
print()

for x in range(1, 11):
    for y in range(1, 6):
        print(x, y,)
    print()

linha_e_coluna = [
    (x, y)
    for x in range(1, 11)
    for y in range(1, 6)
]
p(linha_e_coluna)
print()

print('LISTCOMPREHESION COM STRINGS       ')

nome = 'Hebert Brito'
numero_de_letras = 1
# novo_nome = [n for n in nome]
# novo_nome = ''.join([n for n in nome]).upper()
novo_nome = '.'.join([
    nome[indice: indice + numero_de_letras]
    for indice in range(0, len(nome), numero_de_letras)



])
print(novo_nome)

name = ['hebert', 'alisson', 'dora', 'fabia', 'brito']
new_name = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'  # deixa a ultima letra MAIUSCULA
    for nome in name]
print(new_name)
print()

linha = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [(valor, valor2) for valor in linha for valor2 in range(3)]
print(ex1)
print()

nomess = ['hebert', 'heliane', 'hercules']
nommes = [letras.replace('e', '@').upper() for letras in nomess]
print(nommes)
print()

tupla = (
    ('nome', 'hebert'),
    ('nome', 'alisson'),
    ('nome', 'dora'),

)
extuple_1 = [(x, y) for x, y in tupla]
extupla = dict(extuple_1)
print(extupla['nome'])
