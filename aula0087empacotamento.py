"""
Introdução ao empacotamento e desempacotamento
"""
'''_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)'''
'''nomes = ['maria', 'HEBERT', 'luiz', 'ANTONIO',
         'JOSUE', 'Dora', 'Sergio', 'ana']

nome_1, nome_2, nome_3 = ['maria', 'HEBERT', 'luiz',
                          'ANTONIO', 'JOSUE', 'Dora', 'Sergio', 'ana']
print(nome_3.upper())
print(nome_2.lower())
print(nome_1.capitalize())'''

nome_1, *_ = ['maria', 'HEBERT', 'luiz',
              'ANTONIO', 'JOSUE', 'Dora', 'Sergio', 'ana']
# *_ => INDICA QUE EXISTE UMA VARIAVEL AMS ELA NAO VAI SER USADA...
print(nome_1)
print()
print(_)
