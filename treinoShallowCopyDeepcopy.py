import copy

print('   APARENAS UMA REFERENCIA    ')
pessoas = ['hebert', 'alisson', 'dora']
# pessoas[1] = 'Brito'
pessoas_referencia = pessoas
pessoas_referencia[0] = 'fabia'
print(pessoas)
print(pessoas_referencia)
"""
['fabia', 'alisson', 'dora']
['fabia', 'alisson', 'dora']
ESTA APONTANDO PRO MESMO LUGAR NA MEMORIA MUDANDO UMA MUDA A OUTRA
ISSO ACONTECE COM DADOS MUTAVEIS
"""
print('   SHALLOW COPY    ')

pessoas = ['hebert', 'alisson', 'dora', ['FABIA', 'BRITO']]

pessoas_referencia = pessoas.copy()
pessoas_referencia[0] = 'fabia'
pessoas_referencia.append('TIAGO')
print(pessoas)
print(pessoas_referencia)
""" 
   SHALLOW COPY    
['hebert', 'alisson', 'dora'] ORIGINAL
['fabia', 'alisson', 'dora'] COPIA

pessoas_referencia ==> RECEBE UMA COPIA DE PESSOAS MAS AQUI
SOMENTE pessoas_referencia FOI ALTERADO AS COPIA ORIGINAL PERMANECE IGUAL
"""
print('   CASTING DE TUPLE PRA LIST    ')

pessoas = ('hebert', 'alisson', 'dora')

pessoas_referencia = list(pessoas)
pessoas_referencia[0] = 'fabia'
print(pessoas)
print(pessoas_referencia)

print('   DEEP COPY    ')

pessoas = ['hebert', 'alisson', 'dora', ['FABIA', 'BRITO']]

pessoas_referencia = copy.deepcopy(pessoas)
pessoas_referencia[3][1] = 'OTACILIO'
pessoas_referencia[0] = 'fabia'
pessoas_referencia.append('TIAGO')
print(pessoas)
print(pessoas_referencia)
"""  
ANTES DA DEEPCOPY
['hebert', 'alisson', 'dora', ['FABIA', 'OTACILIO']]
['hebert', 'alisson', 'dora', ['FABIA', 'OTACILIO']]

  DEEP COPY    
['hebert', 'alisson', 'dora', ['FABIA', 'BRITO']]
['hebert', 'alisson', 'dora', ['FABIA', 'OTACILIO']]

NA DEEPCOPY OS VALORES DAS LISTA ORIGINAL SE MANTEM E SOMENTE A COPIA PODE SER ALTERADA 

"""

people = {
    'primeiro_nome': 'hb',
    'sobrenome': 'brito',
    'endereco': [
        {'rua1': 'mozart lucena', 'numeeo': 1660},
        {'rua2': 'palmacia', 'numero': 65},
    ]

}
# copia_people = people.copy()
copia_people = copy.deepcopy(people)
copia_people['primeiro_nome'] = 'Tiago'
print(people)
print(copia_people)
