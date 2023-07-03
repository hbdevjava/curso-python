"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

a, b, *_ = 1, 2, 3, 4, 5
print(a, b, _)


def somaa(a, b):
    return a + b


def soma(*args):

    total = 0  # ACUMULADOR
    for numeros in args:
       # print('total ', total, '+', numeros) # MOSTRA PASSO A PASSO DO ACUMULADOR
        total += numeros
        # print(total)
    return total


soma_1 = soma(1, 2, 3, 4, 5, 6)
print(soma_1)


# def soma(x, y):
# retorna x + y

'''def soma(* args):
    total = 0

    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

outra_soma = soma()
print(outra_soma)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

# print(soma(números))
print(numeros)'''
