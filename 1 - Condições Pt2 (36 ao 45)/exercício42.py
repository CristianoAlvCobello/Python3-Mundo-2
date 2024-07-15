lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))

vermelho = '\033[1;31m'
roxo = '\033[1;35m'
verde = '\033[1;32m'
azul = '\033[1;34m'
limpar ='\033[m'

if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado1+lado2:
    print('\nOs lados {}PODEM{} formar um triângulo '.format(verde,limpar), end='')
    
    if lado1 == lado2==lado3:
        print('{}EQUILÁTERO{}'.format(roxo,limpar))
    
    elif lado1 != lado2 and lado2 != lado3:
        print('{}ESCALENO{}'.format(verde,limpar))
    
    else:
        print('{}ISÓSCELES{}'.format(azul, limpar))
else:
    print('Os lado {}NÃO PODEM{} formar um triângulo'.format(vermelho,limpar))
