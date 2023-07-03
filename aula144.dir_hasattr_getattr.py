import sys

"""        
dir, hasattr e getattr em Python

tudo no Python é um objeto

DIR: ELE CHECA QUAIS OS METODOS CONTIDOS NO OBJETO EX:print(nome.) == DIR TRAS TUDOS OS ATRIBUTOS QUE ESTAO DEFINIDOS DENTRO DO METODOS

HASATTR : CHECA DINAMICAMENTE SE O ATRIBUITO EXISTE DENTRO DO OBJETO

GETATTR : EXECUTA DINAMICAMENTE O ATRIBUTO MOSTRADO PELO hasattr

"""


nome = 'Hebert'
metodo = 'upper'
# metodo = 'upper1'

if hasattr(nome, metodo):
    print('ESSE METODO EXISTE ')
    print(getattr(nome, metodo)())
    # print(nome.upper())
else:
    print('NAO EXISTE ESSE METODO')
print()

"""
145. Mais detalhes sobre Iterables e Iterators (Iteráveis e Iteradores)
GENERATOR EXPRESSION, ITERABLES E ITERATORS EM PYTHON

TEM ___ITER____ E ___NEXT___ (NOME DESSA FUNÇAO É DANDER)

ITERAVEL TEM A RESPONSABILIDADE DE DETER OS VALORES SEQUENCIALMENTE E E UNICA RESPOSABILIDADE DO ITERATOR É ME ENTREGAR UM VALOR POR VEZ 
(ELE NAO SABE EUM É O PRIMEIRO, O ULTIMO, O DO MEIO... NEM TAMANHO) ELE SO TE ENTREGA O PROXIMO  ex: print(netx(iterador)) ==       Eu
                    Tenho
                    __iter___

#TODO GENERATOR É UM ITERATOR MAS NENHUM ITERATOR É UM GENERATOR
GENERATOR É UMA FUNÇAO QUE PAUSA... 
ELE NAO SABE NADA SOBRE O ELEMENTO (TAMANHO, INDICE, PRIMEIRO OU ULTIMO)

"""

iterador = ['Eu',  'Tenho', '__iter___']
iterador = iterador.__iter__()
generator_1 = (n for n in range(10))
generator_2 = [n for n in range(10)]
print(generator_1)
print(generator_2)
# AQUI O GENERATOR SEGURA OS VALORES ATE QUE CHAME EX: print(next(generator_1))
print(sys.getsizeof(generator_2))
# AQUI A LISTA ESTA TODA NA MEMORIA DO PC (print(sys.getsizeof(generator_1)) MOSTRA O TAMANHO DO ARQUIVO EM BYTES)
print(sys.getsizeof(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
# print(next(generator_1))
# print(next(generator_1))
# print(next(generator_1))


print(next(iterador))
print(next(iterador))
print(next(iterador))
# print(next(iterador))
print()
# Introdução às Funções do gerador em Python
# gerador = (n FOR n IN RANGE(1000000))
# StopIteration: ACABOU


def gererator(y=0):
    yield 1  # PAUSA
    print('CONTINUANDO...')
    yield 'hb'.upper()  # PAUSA
    print('CONTINUANDO...')
    yield 3  # PAUSA
    print('MAIS UMA VEZ...')
    yield 'son'.upper()  # PAUSA
    print('VOU ACABAR E LEVANTAR A EXCEÇÃO...(StopIteration)')
    return 'ACABOU'


gen = gererator(y=0)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
print('POREM NO FOR ELE NAO LEVANTA EXCEÇÃO PQ O FOR JA TRATA ELA INTERNAMENTE')
print()


def gererator_4(y=0, maximum=10):
    while True:
        yield y
        y += 1

        if y > maximum:
            return


gen_1 = gererator_4(y=0, maximum=10)
for valor in gen_1:
    print(valor)

print()
