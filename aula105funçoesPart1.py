"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)
'''
DOCSTRINGS:

soma(8, 8, 9) = soma() takes 2 positional arguments but 3 were given
                soma () leva 2 argumentos posicionais, mas 3 foram fornecidos




'''




import random
def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} é {s}')


def saudaçao(nome='Sem nome'):
    print(f'Olá, {nome}!')


def contador(*num):
    print(num)


def dobrar(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


def soma1(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


def soma2(a, b):
    print(f'{a=} + {b=} =', a + b)


soma2(1, 1)


saudaçao('Luiz Otávio')
saudaçao('Maria')
saudaçao('Helena')
saudaçao()
print()

soma(5, 5)
soma(a=5, b=5)
print()

contador(1, 2, 3)
contador(7, 82, 39)
contador(18, 25, 31)
contador('hb', 'son', 1, 7, 'Lisboa')

valores = [random.randint(0, 5), random.randint(0, 5), random.randint(
    0, 5), random.randint(0, 5), random.randint(0, 5)]
print(valores)
dobrar(valores)
print(valores)

soma1(2, 7)
soma1(4, 78, 9654)
soma1(7, 8, 9, 4, 5, 6)


def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
