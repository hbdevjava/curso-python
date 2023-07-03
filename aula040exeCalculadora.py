'''while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite um numero: ')
    operador = input('Qual Operador? [+-*/]: ')

    numeros_validos = None
    numero_1_int = 0
    numero_2_int = 0

    try:
        numero_1_int = float(numero_1)
        numero_2_int = float(numero_2)
        numeros_validos = True
        ...
    except:
        numeros_validos = None
        ...
    if numeros_validos is None:
        print('Um ou ambos dos numeros nao sao digitados...')
        continue
    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos and len(operador) > 1:
        print('Operador INVALIDO...')
        continue
    print('Realizando sua conta... Cofira o resultado a baixo...')
    if operador == '+':
        print(f'{numero_1_int} + {numero_2_int} =',
              numero_1_int + numero_2_int)
        ...
    elif operador == '-':
        print(f'{numero_1_int} - {numero_2_int} =',
              numero_1_int - numero_2_int)
        ...
    elif operador == '*':
        print(f'{numero_1_int} * {numero_2_int} =',
              numero_1_int * numero_2_int)
        ...
    elif operador == '/':
        print(f'{numero_1_int} / {numero_2_int} =',
              numero_1_int / numero_2_int)
        ...
    else:
        print('Nao Deveria chegar aqui...')

    sair = input('Quer sair [S/N]: ').capitalize().startswith('Sair')
    print(sair)
    if sair is True:
        break
print('acabou...')'''

################################################################################
################################################################################

print('{:=^60}'.format(' HBCalc com while '))
while True:
    num_1 = input('Digite o primeiro numero: ')
    operador = input('Escolha um operador [+-*/]: ')
    while operador not in '+-*/':
        print('Operador Invalido')
        operador = str(input('Escolha um operador [+-*/]: '))

    num_2 = input('Digite o segundo numero: ')

    numero_1 = 0
    numero_2 = 0
    numero_validos = None

    try:
        numero_1 = float(num_1)
        numero_2 = float(num_2)
        numero_validos = True

        ...
    except:
        numero_validos = None
        print('Digite algo valido...')
        continue

    # print('Seu Resultado sera apresentado a baixo...')
    if operador == '+':
        print(
            f'O Resultado de {numero_1:.0f} + {numero_2:.0f} =', numero_1 + numero_2)
    elif operador == '-':
        print(
            f'O Resultado de {numero_1:.0f} - {numero_2:.0f} =', numero_1 - numero_2)
    elif operador == '*':
        print(
            f'O Resultado de {numero_1:.0f} * {numero_2:.0f} =', numero_1 * numero_2)
    elif operador == '/':
        print(
            f'O Resultado de {numero_1:.0f} / {numero_2:.0f} =', numero_1 / numero_2)
    else:
        print('Valor invalidos...')
    sair = str(input('Quer sair do programa [S/N]:')).upper().startswith('S')
    if sair is True:
        break
print('Obrigado e Volte Sempre!!!!')
