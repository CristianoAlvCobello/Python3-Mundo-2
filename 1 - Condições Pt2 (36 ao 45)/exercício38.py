vermelho = '\033[31m'
azul = '\033[34m'
roxo = '\033[35m'
limpar = '\033[m'

numero1 = int(input('{}Digite o número 1: {}'.format(azul,limpar)))
numero2 = int(input('{}Digite o número 2: {}'.format(vermelho,limpar)))

if numero1 > numero2:
    print('\n{}O número 1 é maior{}'.format(azul,limpar))

elif numero2 > numero1:
    print('\n{}O número 2 é maior{}'.format(vermelho,limpar))

else:
    print('\n{}Os dois são iguais{}'.format(roxo,limpar))
    