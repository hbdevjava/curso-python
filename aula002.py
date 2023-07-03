"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
'''numero_str = input('Digite um numero:  ')

try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print(f'{numero_int} é PAR')
    elif numero_int % 2 == 1:
        print(f'{numero_int} é IMPAR')
except:
    print('Esse numero nao é um INTEIRO')

print('-='*40)'''
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''entrada = input('Que horas sao?: ')
try:
    hora_certa = int(entrada)
    if 0 < hora_certa <= 11:
        print('BOM DIA!!!!')
    elif 12 <= hora_certa < 17:
        print('BOA TARDE!!!')
    elif 18 <= hora_certa <= 22:
        print('Boa Noite!!!')
    else:
        print('HORA DESCONHECIDA...')
except:
    print('DIGITE APENAS HORARIO CONHECIDO')
print('-='*40)'''


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

'''nome = input('Digite seu nome: ')
nome_tamanho = len(nome)

if nome_tamanho > 1:
    if nome_tamanho <= 4:
        print('Seu nome é curto')
    elif 5 <= nome_tamanho <= 6:
        print('Seu nome é normal')
    else:
        print('eu nome é muito grande')

else:
    print('Digite pelo menos duas letra')'''
