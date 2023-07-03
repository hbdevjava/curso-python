"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
'''string = 'hebert brito'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string.capitalize())
print(string.upper())
print(string.lower())
print(string.zfill(20))
print(outra_variavel)'''

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
'''condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
    if nome == '0':
        break

print('Acabou') '''

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
'''contador = 1

while contador <= 10:
    print(contador, end=' ')
    contador += 1
print('Acabou')

print('-='*30)'''

'''n = 1
par = impar = 0
while n != 0:
    n = input('Digite um numero: ')
    n_1 = int(n)
    if n_1 % 2 == 0:
        par += 1
    else:
        impar += 1
    if n_1 == 999:
        break

print(f'vc digitou {par} numeros Pares e {impar} numeros Impares')'''

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
'''contador = 17
contador %= 2 #par ou impar
print(contador)
'''
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
'''contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue  # PULA UMA EXECUÇAO EX:1, 2, 3, 4, 5, 7, 8... (6)?

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)

        continue

    print(contador)

    if contador == 30:
        break


print('Acabou')'''

"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
'''qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')'''
# .......01234567891011...
'''nome = 'hebert brito'
tamanho_nome = len(nome[:-1])  # menos 1 pq tem um espaço
print(nome)
print(tamanho_nome)
print(nome[4])'''

'''frase = 'O Python é uma linguagem de programaçao multiparadigma' \
    'Python foi criado por Guido Van Rossum'


i = 0
a_letra_apareceu_mais_vezes = ''
qtd_da_letra_apareceu_mais_vezes = 0


while i < len(frase):
    frase_iterada = frase[i]
    i += 1

    if frase_iterada == ' ':  # esse cod captura q qtd de espaços contando +1
        continue

    qtd_apareceu_primeiro = frase.count(frase_iterada)

    if qtd_da_letra_apareceu_mais_vezes < qtd_apareceu_primeiro:
        qtd_da_letra_apareceu_mais_vezes = qtd_apareceu_primeiro
        a_letra_apareceu_mais_vezes = frase_iterada

    i += 1


print(
    'A letra que apareceu mais vezes foi '
    f'({a_letra_apareceu_mais_vezes}) que apareceu '
    f'{qtd_da_letra_apareceu_mais_vezes}x')'''

texto = 'Python'

i = 0
tamanho_nome = len(texto)
while i < tamanho_nome:
    print(texto[i], '=', i)
    i += 1

print('Acabou...')
