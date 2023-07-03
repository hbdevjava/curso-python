"""       
isinstace - para saber se objeto é de determinado tipo
isinstace checa se é uma instancia


"""
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, dict):
        print('DICT')
        item['nome'] = 'hebert'
        item['sexo'] = 'masculino'
        print(item)
        print()

    elif isinstance(item, list):
        print('LIST')
        item.append(41)
        print(item)
        print()

    elif isinstance(item, str):
        print('STR')
        # item.upper()
        print(item.upper())
        print()
        print()

    elif isinstance(item, (int, float)):
        print('INT OR FLOAT')
        print(item, item * 2)
        print()

    else:
        print('OUTRO')
        print(item)
