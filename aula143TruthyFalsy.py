# Valores Truthy e Falsy, Tipos Mutáveis ​​e Imutáveis
# Mutáveis ​​[] {} set()
# Imutáveis ​​() "" 0 0.0 Nenhuma False range(0, 10)
# CADA UM DESSES CONJUNTOS A BAIXO SE FOR VAZIO RETURN FALSE QUALQUE CONJUNTO DESSE SE TIVER UMA ESPAÇO É RETURN TRUTHY (TB ADD 0)
list = []
dict = {}
set = set()
tuple = ()
str = ''
int = 0
float = 0, 0
nada = None
falso = False
range = range(0)


def falsey(valor):
    return 'falsy' if not valor else 'truthy'


print(f'TEST', falsey('TEST'))
print()
print(f'{list =}', falsey(list))
print()
print(f'{dict =}', falsey(dict))
print()
print(f'{set =}', falsey(set))
print()
print(f'{tuple =}', falsey(tuple))
print()
print(f'{str =}', falsey(str))
print()
print(f'{int =}', falsey(int))
print()
print(f'{float =}', falsey(float))
print()
print(f'{nada =}', falsey(None))
print()
print(f'{falso =}', falsey(False))
print()
print(f'{range =}', falsey(range))
print()
