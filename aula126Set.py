# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados

hb = set()  # vazio
hb_1 = {'hb', 'son', 1, 2, 3, 3, 3}  # com elementos
print(hb)
print(hb_1)

l1 = [1, 1, 2, 3, 3, 3, 4, 5]
print(5 not in l1)
print(5 in l1)
print(8 not in l1)
s1 = set(l1)
l2 = list(s1)
print(l2)
s_3 = set('hebert')
print('h' in s_3)
for nome in s_3:
    print(nome, end=' ')
print()
s_4 = {'hebert'}
for nome in s_4:
    print(nome, end=' ')

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# Métodos úteis:
# add, update, clear, discard
print()
s_1 = set()
s_1.add('hb')
s_1.add('son')
s_1.update(('OlaMUndo', 11, 12))
# s_1.update('dora')
print(s_1)
s_1.discard('hb')
s_1.discard('dora')
print(s_1)
print()
print(1, 2, 3, '|', 2, 3, 4)
# Operadores úteis:
# união | união (union) - Une
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
set_3 = set_1 | set_2
print(set_3)
# intersecção & (intersection) - Itens presentes em ambos
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
set_3 = set_1 & set_2
print(set_3)
# diferença - Itens presentes apenas no set da esquerda
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
set_3 = set_1 - set_2
print(set_3)

# diferença simétrica ^ - Itens que não estão em ambos
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
set_3 = set_1 ^ set_2
print(set_3)

letras = set()
while True:
    palavra = input('Digite algo: ')
    letras.add(palavra.upper())

    if 'HB' in letras:
        print('Parabens')
        break

    print(letras)
