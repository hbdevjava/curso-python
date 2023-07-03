import emoji
print('{:=^100}'.format(' Resoluçao 1 '))
perguntas = [
    {'Pergunta': 'Qual a Capital do Ceara',
     'Opçao': ['Natal', 'Fortaleza', 'Sao Luiz', 'Recife'],
     'Resposta': 'Fortaleza',
     },

    {'Pergunta': 'Qual o Maior Pais da America do Sul',
     'Opçao': ['Argentina', 'Chile', 'Equador', 'Brasil'],
     'Resposta': 'Brasil',
     },

    {'Pergunta': 'Em Qual America Fica Localizada o Peru',
     'Opçao': ['America do Sul', 'America do Norte', 'America Central'],
     'Resposta': 'America do Sul',
     }
]
acerto = erros = 0
escolha = ''
while True:
    try:

        print('Pergunta 1: Qual a Capital do Ceara??')
        if escolha != 'Fortaleza':
            print('''
[1] Natal
[2] Fortaleza
[3] Sao Luiz
[4] Recife ''')
            print()
            escolha = int(input('Escolha uma opçao. '))
            if escolha == 2:
                print(emoji.emojize("Voce Acertou :thumbsup:", language='alias'))
                acerto += 1
            else:
                print(emoji.emojize("Voce Errou :polegar_para_baixo:", language='pt'))
                erros += 1
        print()

        print('Pergunta 2: Qual o Maior Pais da America do Sul??')
        if escolha != 'Brasil':
            print('''
[1] Argentina
[2] Chile
[3] Equador
[4] Brasil''')
            print()
            escolha = int(input('Escolha uma opçao. '))
            if escolha == 4:
                print(emoji.emojize("Voce Acertou :thumbsup:", language='alias'))
                acerto += 1
            else:
                print(emoji.emojize("Voce Errou :polegar_para_baixo:", language='pt'))
                erros += 1
        print()

        print('Pergunta 3: Em Qual America Fica Localizada o Peru')
        if escolha != 'America do Sul':
            print('''
[1] America do Sul
[2] America do Norte
[3] America Central 
[4] Nenhuma das Opções
''')
            print()
            escolha = int(input('Escolha uma opçao. '))
            if escolha == 1:
                print(emoji.emojize("Voce Acertou :thumbsup:", language='alias'))
                acerto += 1
            else:
                print(emoji.emojize("Voce Errou :polegar_para_baixo:", language='pt'))
                erros += 1

            print()
            print(f'Vc acertou {acerto} e errou {erros}')
            if acerto > erros:
                print(emoji.emojize(
                    "Feliz por Você:red_heart:", variant="emoji_type"))
            else:
                break

        break
    except:
        print()

        print('DIGITE APENAS NUMEROS...')
        print()
    continue

print('{:=^100}'.format(' Resoluçao do Professor '))

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
     'Opçao': ['America do Sul', 'America do Norte', 'America Central'],
     'Resposta': 'America do Sul',
     }
]
qtd_acertos = qtd_erros = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opçao']
    for i, opcao in enumerate(opcoes):
        print(f'({i})', opcao)
    print()

    escolha = input('Escolha uma opçao: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        print(emoji.emojize("Voce Acertou :thumbsup:", language='alias'))
        print(emoji.emojize(
            "Feliz por Você:red_heart:", variant="emoji_type"))
        qtd_acertos += 1
    else:
        print(emoji.emojize("Voce Errou :polegar_para_baixo:", language='pt'))
        qtd_erros += 1

    print('Vc acertou', qtd_acertos)
    print('de', len(perguntas), ' pergunas..')

print()
print('FIM DO PROGRAMA')
