from random import randint

contador = 0

while True:
    usuario = int(input('\nDigite seu número: '))
    maquina = randint(0,10)

    soma = usuario+maquina
    resposta = ' '

    while resposta not in 'pi':

        resposta = str(input('Par ou Impar(p/i)? ')).strip().lower()

    print(f'\nVocê: {usuario}')
    print(f'Máquina: {maquina}')
    if resposta == 'p':
        if soma%2 == 0:
            print('\033[1;32mVocê Ganhou\033[m')
            soma = 0
            contador = contador+1
        else:
            print('\033[1;31mVocê perdeu\033[m')
            break

    if resposta == 'i':
        if soma%2 != 0:
            print('\033[1;32mVocê Ganhou\033[m')
            print(maquina)
            contador = contador+1
            soma = 0
        else:
            print('\033[1;31mVocê perdeu\033[m')
            break
  
print(f'Você ganhou {contador} vezes consecutivas')
