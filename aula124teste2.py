import emoji
perguntas = [
    {'Pergunta': 'Qual a Capital do Ceara? ',
     'Opçao': ['Natal', 'Fortaleza', 'Sao Luiz', 'Recife'],
     'Resposta': 'Fortaleza',
     },

    {'Pergunta': 'Qual o Maior Pais da America do Sul? ',
     'Opçao': ['Argentina', 'Chile', 'Equador', 'Brasil'],
     'Resposta': 'Brasil',
     },

    {'Pergunta': 'Em Qual America Fica Localizada o Peru? ',
     'Opçao': ['America do Sul', 'America do Norte', 'America Central', 'Nenhuma Opcao'],
     'Resposta': 'America do Sul',
     }
]
qtd_acerto = qtd_erro = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opçao']
    for i, opcao in enumerate(opcoes):
        print(f'({i})', opcao)
    print()

    escolha_opcao = input('Escolha uma das Opções: ')

    acertou = False
    escolha_opcao_int = None
    qtd_opcoes = len(opcoes)

    if escolha_opcao.isdigit():
        escolha_opcao_int = int(escolha_opcao)

    if escolha_opcao_int is not None:
        if escolha_opcao_int >= 0 and escolha_opcao_int < qtd_opcoes:
            if opcoes[escolha_opcao_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print(emoji.emojize("Voce Acertou :thumbsup:", language='alias'))
        print(emoji.emojize(
            "Feliz por Você:red_heart:", variant="emoji_type"))
        qtd_acerto += 1
    else:
        print(emoji.emojize("Voce Errou :polegar_para_baixo:", language='pt'))
        qtd_erro += 1

    print('Vc acertou', qtd_acerto)
    print('de', len(perguntas), 'perguntas..')

print()
print('FIM DO PROGRAMA')


"""print('Pergunta 1: Qual a Capital do Ceara??')

print('''
[1] Natal
[2] Fortaleza
[3] Sao Luiz
[4] Recife ''')
opcao = input('Escolha uma Opcao: ')


print()
print('Pergunta 2: Qual o Maior Pais da America do Sul??')
print('''
[1] Argentina
[2] Chile
[3] Equador
[4] Brasil''')
opcao = input('Escolha uma Opcao: ')

print()
print('Pergunta 3: Em Qual America Fica Localizada o Peru')
print('''
[1] America do Sul
[2] America do Norte
[3] America Central 
[4] Nenhuma das Opções
''')
"""
