vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
limpar = '\033[m'

numero = int(input('Digite um número: '))
print('{}1 - Binário{} \n{}2 - octal{} \n{}3 - hexadecimal{}'.format(vermelho,limpar,verde,limpar,azul,limpar))
converter = int(input('Qual conversão deseja? '))

if converter == 1:
    print('\n{}Binário:{} {}'.format(vermelho,limpar,bin(numero) [2:]))

elif converter == 2:
    print('\n{}Octal:{} {}'.format(verde,limpar,oct(numero) [2:]))

elif converter == 3:
    print('\n{}Hexadecimal:{} {}'.format(azul,limpar,hex(numero) [2:]))
