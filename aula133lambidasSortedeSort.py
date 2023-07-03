# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
# {'nome': 'Luiz', 'sobrenome': 'miranda'},
# {'nome': 'Maria', 'sobrenome': 'Oliveira'},
# {'nome': 'Daniel', 'sobrenome': 'Silva'},
# {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
# {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
#
# lista.sort(reverse=True)
# classificado(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


# def ordenar(item):
#     return item['sobrenome']


# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

print('-='*60)

lista1 = [1, 2, 5, 6, 8, 7, 3, 0, 77]


def showIt(numeros):
    for num in numeros:
        print(num, end=' ')


# lista1.sort(key=lambda show: show)
l1_1 = sorted(lista1, key=lambda show: show)

showIt(l1_1)
print()
print('-='*60)


def executar(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


print(
    executar(
        lambda x, y: x + y,
        2, 3

    ),

)


# def multiplicador(multiplicador):
#     def multiplicar(numeros):
#         return numeros * multiplicador
#     return multiplicar


duplicar = executar(
    lambda m: lambda n: n * m,
    2

)

print(duplicar(2))

# # lista_1.sort()
# sorted(lista1)  # cria uma copia raza
# lista1.sort(reverse=True)
# print(lista1)

print(
    executar(
        lambda *args: sum(args),
        10, 77, 56, 4785, 2
    )

)
