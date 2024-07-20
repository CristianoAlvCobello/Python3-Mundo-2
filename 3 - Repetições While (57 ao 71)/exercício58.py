from random import randint

usuario = int(input('Digite um número: '))
maquina = randint(0,10)
tentativas = 0

while usuario != maquina:
    print('\n\033[31mERROU\033[m')
    if usuario > maquina:
        print('O número é menor...')
    elif usuario < maquina:
        print('O número é maior...')
    usuario = int(input('Tente de novo: '))
    tentativas = tentativas+1

print('\n\033[1;32mVocê acertou, foram necessárias {} tentativas\033[m'.format(tentativas))
