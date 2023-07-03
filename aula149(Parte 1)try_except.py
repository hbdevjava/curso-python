"""(Parte1) try e except para tratar exceções
TRY, EXCEPT, ELSE E FINALY
python -c 'import this' == chama o zen do python
"Errors should never pass silently.
 Unless explicitly silenced."
 em Python toda exceçao sao classes (exception)
 ZeroDivisionError: division by zero
"""
# a = 18
# b = 0
# c = a / b  # ZeroDivisionError: division by zero

try:
    a = 18
    b = 0
    # print('linha 1'[1000])
    c = a / b

except ZeroDivisionError as error:
    print('MENSAGEM do Erro: ', error)
    print('NOME: ', error.__class__.__name__)
except NameError as error:
    print('MENSAGEM do Erro: ', error)
    print('NOME: ', error.__class__.__name__)
except (TypeError, IndexError) as error:
    print('TypeError or IndexError')
    print('MENSAGEM: ', error)
    print('NOME: ', error.__class__.__name__)
except Exception:
    print('Error is not found')
print('CONTINUA')
print()

# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
print()
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e, 'aqui')
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')
