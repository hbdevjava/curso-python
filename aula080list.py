def mensagem():
    print()
    print('-='*30)
    print()


"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234 index +
#        -54321 index -
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
print('{:=^60}'.format(' Listas é Mutavel '))
print()

listahb = ['hb', 'alisson', 'dora', 'fabia']
print(listahb, '= lista original')
mensagem()
# print(len(listahb))
listahb[2] = 'janainna'
print(listahb, 'listahb[2] = "janainna"/ = muda o nome da Dora pra janainna')
listahb.append('Lisboa')
mensagem()
# print(listahb[2])
listahb.insert(2, 'dora')
print(listahb,
      ' listahb.insert(2, "dora") = insere o nome Dora na posiçao [2] antes de Janainna')
# print(len(listahb))
mensagem()


lista_hb_2 = ['Fortaleza', 'Sao Paulo', 'Rio de Janeiro', ['Lisboa', 'Porto',]]
print(lista_hb_2, 'Lista dentro de outra LIsta')
print(len(lista_hb_2))
print(lista_hb_2[0].upper())
print(lista_hb_2[3][1].capitalize())
print(lista_hb_2, '= lista_hb_2')
lista_hb_2.pop()
print(lista_hb_2)
lista_hb_2.insert(3, ['Lisboa', 'Porto'])
print(lista_hb_2,
      '= lista_hb_2.insert(3, ["Lisboa", "Porto"]) insere uma lista dentro de outra lista ')
print(len(lista_hb_2))
print('aqui')
# lista_hb_2.sort(reverse=True)
# lista_hb_2.sort(reverse=True) METODO sort(reverse=True) NAO SUPORTA STRINGS
# print(lista_hb_2)
print()
lista_hb_3 = [1, 2, 3, 4, 5, 6]
lista_hb_3.sort(reverse=True)
print(lista_hb_3, '= lista_hb_3.sort(reverse=True), esse metodo nao suporta str')
mensagem()

lista_hb_3.sort()
lista_hb_3[1] = -2
print(lista_hb_3, 'muda o numero 2 por numero -2')
mensagem()

lista_hb_3.insert(1, 2)
print(lista_hb_3, 'Ele insere o numero 2 antes do numero -2')
print('aqui')
print()

print(lista_hb_3)
lista_hb_3.append(7)
print(lista_hb_3)
mensagem()

lista_hb_4 = list()
print(lista_hb_4, ' Lista  4 vazia')
lista_hb_5 = ['CE', 'SP', 'RJ']
lista_hb_6 = ['MA', 'PR', 'RN']
lista_hb_4.append(lista_hb_5)
print(lista_hb_4, ' Lista 4 com lista 5')
lista_hb_4.append(lista_hb_6)
print(lista_hb_4, 'lista 4 com lista 5 e lista 6')
lista_hb_7 = ['hb', 'alisson', 'dora']
lista_hb_8 = ['fabia', 'janainna', 'joao']
lista_hb_5.append(lista_hb_7)
print(lista_hb_4, ' lista 5 com lista 6')

mensagem()
lista_hb_7.append(lista_hb_8)
print(lista_hb_4, 'dentro da lista 5 esta a lista 7 e dentro da 7 a lista 8')
lista_hb_9 = lista_hb_7 + lista_hb_8
print(lista_hb_9)
mensagem()


# lista_hb_3.index(2)
# print(lista_hb_3)


lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))

print('{:=^60}'.format(' Listas é Mutavel '))
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)  # adiciona elemento no final da lista
lista.pop()  # remove o ultimo elemento da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido,', ultimo_valor)
mensagem()
lista_numero = [10, 20, 30, 40, 50]
print(lista_numero)
lista_numero.pop()
print(lista_numero, 'se nao passar o valor do indice pelo parametro ele sempre vai excluir o ultimo valor')
lista_numero.append(60)
print(lista_numero)
lista_numero.pop(0)
print(lista_numero, 'passando parametro ele exclui o valor no indice indicado')
mensagem()
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
print(f'Lista A = {lista_a}')
print(f'Lista B = {lista_b}')
lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
print(lista_c, 'lista_c = lista_a + lista_b')
lista_d = lista_b + lista_a
print(lista_d, 'lista_d = lista_b + lista_a')
lista_a.extend(lista_b)
print(lista_a, 'lista_a.extend(lista_b)', 'A')
lista_b.extend(lista_a)
print(lista_b, 'lista_b.extend(lista_a)', 'B')
lista_c.extend(lista_d)
print(lista_c, 'lista_c.extend(lista_d)', 'C')
lista_d.extend(lista_c)
print(lista_d, 'lista_d.extend(lista_c)', 'D')
mensagem()

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
print('{:=^60}'.format(' COPIA DE Listas é Mutavel '))
lista_a = ['A', 'B', 'C']
# Cria uma copia da lista A e salva como nova lista (caso lista a seja alterada lisba permanece como antes lista_a = ['A', 'B', 'C'])
lista_b = lista_a.copy()
lista_a[0] = 'HSB'
print(lista_a)
print(lista_b)
print()
lista_c = [1, 2, 3]
lista_d = lista_c[:]

lista_c[0] = 33
print(lista_c)
print(lista_d)
mensagem()

# ################ for in com listas ########################333

lista = ['Maria', 'Helena', 'Ana', 'Claudia', 'Rita']
lista.append('joao')
lista.append('Hb')
lista.append('alisson')
lista.append('dora')
del lista[6]
lista.pop()

print('EXERCICIO PROPOSTO')

# print(lista)

i = 0
for nome in lista:
    print(i, '=', nome)
    i += 1

mensagem()


lista = ['Maria', 'Helena', 'Ana', 'Claudia', 'Rita']
lista.append('joao')
lista.append('Hb')
lista.append('alisson')
lista.append('dora')

for i in range(len(lista)):
    print(i, '=', lista[i])  # se nao colocar [i] ele mostra a lista completa
print('Fim....')

mensagem()
