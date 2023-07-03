print('Este módulo se chama', __name__)

correr = True
cansaço = False
cerveja = False
saude = True
while True:
    if correr:
        cansaço = True
        cerveja = True
        saude = False
    else:
        cansaço = False
        cerveja = False
        saude = True
