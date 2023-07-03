def titulo(msg):
    print('-='*30)
    print(msg)


def hb(msg):
    print('-='*30)
    print('{:=^60}'.format(msg))
    print('-='*30)
    print()


def soma(a=0, b=0, c=0):
    """ FAZ A SOMA ENTRE 3 VALORES E MOSTRA O RESULT NA TELA
    :PARAM: PRIMEIRO VALOR
    :PARAM: SEGUNDO VALOR 
    :PARAM: TERCEIRO VALOR
    """
    s = a + b + c
    print(f'Somando os valores {a} + {b} + {c} temos {s}')


hb('PARAMENTROS OPERACIONAIS')

soma(4, 10, 8546)
soma(7, 8, 2)
'''soma(7, 8, 2, 1)
TypeError: soma() takes from 0 to 3 positional arguments but 4 were given
'''
soma()

hb('ESCOPO DE VARIAVEIS')

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é acessível.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    # global x
    x = 10

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(x, y, '(local_2)')

    outra_funcao()
    print(x, '(local_3)')


print(x, '(x=global)')

escopo()
print(x, '(local_1)')


hb = print('hb')
print(hb)


def somahb(a, b):
    return (a + b)


hb1 = somahb(1, 1)
hb2 = somahb(2, 2)
print(hb1 + hb2)
