import re
import sys
# from random import randint
import random

'''
DOCSTRINGS dessa Aula:

SOBRE OS IMPORTS: CASO IMPORTE SOMENTE A UMA FUNÇAO 'from random import randint' DO MODULO TENHO QUE ATRIBUIR UMA VARAVEL A ELE, CASO IMPORTE O MODULO COMPLETO 'import random' CONSIGO USAR DIRETAMENTE NO PRINT()

EX: from random import randint
h = randint(0, 9)
print(h)
sys.exit()

EX: import random
print(random.randint(0, 9))

SOBRE FOR: QUANDO NAO FOR USAR UMA VARIAVEL SE COLOCA UM '_'

EX: for _ in range(10):

'''
for _ in range(10):

    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10

    result_digito_1 = 0
    for digito in nove_digitos:
        # CAST (int(digito_1)
        result_digito_1 += (int(digito) * contador_regressivo_1)
        contador_regressivo_1 -= 1

    digito_1 = ((result_digito_1 * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    result_digito_2 = 0
    for digito in dez_digitos:
        # CAST (int(digito_2)
        result_digito_2 += (int(digito) * contador_regressivo_2)
        contador_regressivo_2 -= 1

    digito_2 = ((result_digito_2 * 10) % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_sistema = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_sistema)
    print()
