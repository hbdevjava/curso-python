import re
import sys


def mensagem():
    print()
    print('-='*30)
    print()


"""
Cálculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.: 746.824.890-70 (746824890)
   10 9  8  7  6  5  4  3  2
*   7 4  6  8  2  4  8  9  0
   70 36 48 56 12 20 32 27 0
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obtenha o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

"""
Cálculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.: 746.824.890-70 (7468248907)
   11 10 9 8 7 6 5 4 3 2
* 7 4 6 8 2 4 8 9 0 7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36 0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obtenha o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
# cpf = '36440847007' # Esse CPF gera o primeiro dígito como 10 (0)
'''cpf_usuario = '746.824.890-70'\
    .replace(',', '')\
    .replace('.', '')\
    .replace('-', '')
print(f'CPF envido pelo usuario: {cpf_usuario}')'''
entrada = input('CPF: ')
cpf_usuario = re.sub(
    r'[^0-9]',  # de zero a nove substitua tudo que nao for numero ^
    '',  # substitua por espaço vazio
    entrada
)  # expressao regular

entrada_sequencial = entrada == entrada[0] * len(entrada)
# entrada_sequencial = ENTRADA E VERIFICA SE O PRIMEIRO VALOR 'entrada[0]' É IGUAL AOS DEMAIS 'len(entrada)' EM ENTRADA

if entrada_sequencial:
    print('VOCE DIGITOU VALORES SEQUÊNCIAIS...')
    sys.exit()


print(f'CPF envido pelo usuario: {cpf_usuario}')

print('PRIMEIRO DIGITO')
nove_digitos = cpf_usuario[:9]

contador_regressivo_1 = 10


# for i, digito in enumerate(nove_digitos):
# print(i, digito)

'''i = 0
for digito_1 in nove_digitos:
    print([i], digito_1, contador_regressivo_1)
    contador_regressivo_1 -= 1
    i += 1'''

result_digito_1 = 0
for digito in nove_digitos:
    # CAST (int(digito_1)
    result_digito_1 += (int(digito) * contador_regressivo_1)
    contador_regressivo_1 -= 1
print(result_digito_1)
print()
digito_1 = ((result_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print()
print(f'O Primeiro Digito é : {digito_1}')

mensagem()

print('SEGUNDO DIGITO')

cpf_usuario = '74682489070'
dez_digitos = cpf_usuario[:10]
contador_regressivo_2 = 11

'''i = 0
for digito in dez_digitos:
    print([i], digito, contador_regressivo_2)
    contador_regressivo_2 -= 1
    i += 1'''

result_digito_2 = 0
for digito in dez_digitos:
    # CAST (int(digito_2)
    result_digito_2 += (int(digito) * contador_regressivo_2)
    contador_regressivo_2 -= 1
print(result_digito_2)
print()
digito_2 = ((result_digito_2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'O Segundo Digito é : {digito_2}')
mensagem()

cpf_sistema = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_sistema)

if cpf_usuario == cpf_sistema:
    print(f'O CPF:{cpf_usuario} é VALIDO')
else:
    print('Cpf INVALIDO')

print()
