"""
Operação ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
"""
# condição = 10 == 11
# variavel = 'Valor' if condição else 'Outro valor'
# print(variavel)
# dígito = 9 # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
'''print ( 'Valor'  if  False  else  'Outro valor'  if  False  else  'Fim' )'''


# print('valor' if False else 'outro valor')

condiçao = 'hb' == 'hb'
variavel = 'valor' if condiçao else 'outro valor'
print(variavel)

digito = 2

# DUAS FORMAS DE SE FAZER A MESMA COISA
novo_digito_1 = digito if digito <= 9 else 0
# novo_digito_1 recebe o digito se o digito for menor ou igual a 9 se for maior ele recebe zero
novo_digito_2 = 0 if digito > 9 else digito
# novo_digito_2 recebe zero se o digito for maior que 9 se for menor ele recebe o digito
print(novo_digito_1)
print(novo_digito_2)
