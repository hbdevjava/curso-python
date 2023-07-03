import os
lista = list()

opçao = 0
try:
    while opçao != 4:
        print('''
[1] Inserir compras ao Carrinho
[2] Excluir Item do Carrinho
[3] Ir para o Carrinho
[4] Encerra Compras''')
        print()

        opçao = int(input('Selecione uma opçao: '))
        if opçao == 1:
            lista.append(str(input('O que seja comprar? ')))
            while True:
                resposta = str(input('Algo Mais? [S/N]? '))
                if resposta in 'sim':
                    lista.append(str(input('O que mais Deseja compra? ')))
                if resposta in 'nao':
                    break

        elif opçao == 2:
            if len(lista) == 0:
                print('Nao Existem Produtos em seu Carrinho...')
                continue
            mercadoria_excluir = str(
                input('Qual item deseja retirar do Carrinho??: '))
            if mercadoria_excluir in lista:
                lista.remove(mercadoria_excluir)
                print(f'{mercadoria_excluir} Excluido')
            elif mercadoria_excluir is not lista:
                print(f'Nao exite {mercadoria_excluir} no Carrinho...')

        elif opçao == 3:
            if len(lista) == 0:
                print('Seus Carrinho esta VAZIO!!!')
                print('Escolha a opçao de numero 1 e começe suas compras...')
            else:
                if len(lista) < 1000:
                    print(f'Existem {len(lista)} itens escolhidos')
                elif len(lista) == 1:
                    print(f'Foi escolhido apenas {len(lista)} item')
                # print(f'Item do seu Carrinho = {lista}')

                print(f'Itens do seu Carrinho = {lista}')

        elif opçao == 4:
            print('Voce comprou...')
            for itens in lista:
                print(itens)
            print()
            print('Obrigado e volte sempre!!!!')
            lista.clear()
except:
    print('DIGITE APENAS NUMEROS ')

print('Fim do Programa')
print()

print('SOLUCAO DO PROFESSOR')

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')
