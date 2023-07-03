# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0 1
    ['Maria', 'Helena'],   # 0
    # 0
    ['Elaine'],
    # 0 1 2
    ['Luiz', 'João', 'Eduarda']
]
'''print(*lista, sep='\n')
print(*string, sep=',')
print(*tupla)'''
print(*salas, sep='\n')

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

# print(* salas, set=' \ n ')
