""" while/else """
from time import sleep
string = 'hebert brito'

i = 0
while i < len(string):
    sleep(0.5)
    letra = string[i]
    i += 1
    if letra == ' ':
        break
    print(letra, end='')

else:
    print('\nNão encontrei um espaço na string a cima...')
print('\nFora do while.')
