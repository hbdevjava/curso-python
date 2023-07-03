print('Hello World!!!')
'''print('Hebert Brito')
print('Gonna live in Lisbon')
print('-='*30)
primeiro_valor = input('Digite um numero:  ')
segundo_valor = input('Digite o segundo numero:  ')
if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor} maior ou igual ao  {segundo_valor} ')

else:
    print(f'{segundo_valor} maior que o {primeiro_valor}')'''
'''print('-='*30)
entrada = input('Digite [E]ntrar or [S]air: ')
senha_digitada = int(input('Digite sua senha: '))

senha_permitida = 123456
if entrada == 'e' or entrada == 'E' and senha_digitada == senha_permitida:
    print('Acesso Permitido')
else:
    print('Acesso NEGADO')'''

'''nome = input('Digite seu nome: ')
encontrar = input('Digite o que vc deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')'''

# ***************** FATIAMENTO DE STRINGS *******************

'''nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'seu nome invertido é {nome[::-1]}')
    print(f'seu nome completo é {nome[0:len(nome):1]}')
    if ' ' in nome:
        print('Seu nome contem espaço')
    else:
        print('seu nome nao tem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1:]}')
else:
    print('vc digitou campo vazio')'''


# ************TRATAMENTO DE ERROR:*************

''' SEMPRE QUE O USUARIO TE MANDAR ALGO PELO INPUT ESSE VALOR PRECISA SER TRATADO 
seleciona + f2 vc pode editar todas as strings de uma vez so ,
VARIAVEIS EM MAIUSCULAS SAO CONSTANTES OU SEJA NAO É PRA ATRIBUIR OUTRO VALOR A ELA'''

'''numero_str = input('Vou dobra o numero que vc digitar: ')
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso nao é um errro...')'''

# VARIAVEIS CONTANTES COMPLEXIDADE NO COD AULA 51

'''velocidade = 80
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou = velocidade > RADAR_1
carro_multado_radar_1 = local_carro >= (
    LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou:
    print('Velocidade Maxima Excedida')
if carro_multado_radar_1 and velocidade_carro_passou:
    print('MULTADO')'''
