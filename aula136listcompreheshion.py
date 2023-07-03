import pprint

lista = [num * 2 for num in range(10)]
print(lista)

print('     MAPEAMENTO COM LISTCOMPREHESION ')

produto = [
    {'nome': 'produto_1', 'preco': 200},
    {'nome': 'produto_2', 'preco': 300},
    {'nome': 'produto_3', 'preco': 400},
    {'nome': 'produto_4', 'preco': 500},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] >= 400 else {**produto}
    for produto in produto
]


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
# produto_casa = [
#     {'nome': 'produto_5', 'preco': 600},
#     {'nome': 'produto_6', 'preco': 350},
#     {'nome': 'produto_7', 'preco': 400},
#     {'nome': 'produto_8', 'preco': 850},

# ]

# produto_geral = [{**produto}]
# print(produto_geral)


# print(novos_produtos)
# print(*novos_produtos, sep='\n')
p(novos_produtos)
print()
print('     FILTRO COM LISTCOMPREHESION ')
"""
 O QUE VEM A ESQUERDA DO FOR É MAPEAMENTO E A DIREITA É FILTRO EX:
    novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] >= 400 else {**produto}
    for produto in produto
]
    
    
"""
print()

lista = [num for num in range(11) if num < 5]
print(lista)

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 0.50}
    if produto['preco'] > 300 else {**produto}
    for produto in produto
    if produto['preco'] > 200

]

p(novos_produtos)
print()

# lista_1 = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
lista_1 = [
    (x, y)
    for x in range(3)
    for y in range(3)

]

print(lista_1)
