print('{:=^60}'.format(' MULTIPICADOR '))
print()


def multipicador(*arg):
    total = 1  # todo numero numero * 0 é 0 então na * começa o acumulador com 1
    for num in arg:
        total *= num
    return total


multi = multipicador(2, 2, 2, 2)
print(multi)

multip = multipicador(4, 4)
print(multip)
# multipicador(4, 2)
print()
print('{:=^60}'.format(' PAR OR IMPAR '))

'''def parOrimpar(num):

    if num % 2 == 0:
        print(f'{num} é Par')
        return num
    else:
        print(f'{num} é Impar')
        return num


parOrimpar(3)'''


'''def parOrImpar(num):
    if num % 2 == 0:
        return f'{num} é par'
    else:
        return f'{num} é impar'


exibir = parOrImpar(4589)
print(exibir)'''


def parOrImpar(num):
    if num % 2 == 0:
        return f'{num} é par'
    return f'{num} é impar'


exibir = parOrImpar(4589)
print(exibir)
print()


def parOrimpar(numero):

    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'


hb = parOrimpar(6)
print(hb)

"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}! '
    return saudar


falar_bom_dia = criar_saudacao('bom dia')
falar_boa_tarde = criar_saudacao('Boa tarde')
falar_boa_noite = criar_saudacao('boa noite')

for nome in ['HB', 'Dora', 'Alisson', 'Joao']:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))
    print(falar_boa_noite(nome))

print()


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}! '
    return saudar


s1 = criar_saudacao('bom dia', 'hb')
s2 = criar_saudacao('bom dia', 'dora')

print(s1())
print(s2())

print()
print()


def soma(a,  b):
    s = a + b

    def somar():
        return f'A soma de {a} + {b} = {s}'
    return somar


ss1 = soma(4, 4)
ss2 = soma(4, 5)
ss3 = soma(2, 3)

print(ss1())
print(ss2())
print(ss3())
print()

print('{:=^60}'.format(' exemplo sem CLOSURE '))


def formata_nome(nome):
    nomes = nome.split(' ')
    return nomes[0] + ' ' + nomes[len(nomes) - 1]


nome = formata_nome('hebert de souza brito')
print(nome)

print()
print('{:=^60}'.format(' Exemplo com CLOSURE '))


def nome_completo():
    nome = 'Hebert de Souza Brito'

    def formata_nome():
        nomes = nome.split(' ')
        return nomes[0] + ' ' + nomes[len(nomes) - 1]

    return formata_nome


n = nome_completo()
print(n())
print()


names = ['hb', 'son', 'dora', 'joao']
print(names[len(names) - 1])

numeros = [1, 2, 3, 4, 5, 6]
print(numeros[len(numeros) - 1])
print()


def numeros(valor):
    def novos_numeros():
        a = valor * 2
        b = valor * 3
        c = valor * 4
        return f' {a}, {b}, {c}'
    return novos_numeros


new = numeros(5)
new_1 = numeros(2)
new_2 = numeros(3)
print(new())
print(new_1())
print(new_2())
print()


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
quintuplicar = criar_multiplicador(5)

# multiplicar() missing 1 required positional argument: 'numero' == erro se nao passar os parametros
print(duplicar(5))
print(triplicar(2))
print(quadruplicar(3))
print(quintuplicar(5))
print()


def criar_dobro(soma):
    def criar_dobro_2(valor):
        return valor + soma
    return criar_dobro_2


adicao = criar_dobro(2)

print(adicao(2))
print(adicao(3))
print(adicao(6))
print()


def criar_ola(msg):
    def criar_ola_2(txt):
        return f'{txt} {msg}'
    return criar_ola_2


oi = criar_ola('como vc esta?')
oi_1 = criar_ola('vc esta bem??')
print(oi('hb'))
print(oi_1('hb'))
print()


def sobre_nome(sobrenome):
    def primeiro_nome(nome):
        return f'{nome} {sobrenome}'
    return primeiro_nome


nome_1 = sobre_nome('Brito')
nome_2 = sobre_nome('Rodrigues')

print(nome_1('Hebert'))
print(nome_1('Alisson'))
print()

for nome in ['Hebert', 'alisson', 'Dora']:
    print(nome_1(nome))
    print(nome_2(nome))

print()
