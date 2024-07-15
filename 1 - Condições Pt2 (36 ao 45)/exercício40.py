nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1+nota2)/2
vermelho = '\033[31m'
amarelo = '\033[33m'
verde = '\033[32m'
limpar = '\033[30m'

if media < 5.0:
    print('\nMedia: {}{} Reprovado{}'.format(vermelho,media,limpar))

elif media >= 7.0:
    print('\nMedia: {}{} Aprovado{}'.format(verde,media,limpar))

else:
    print('\nMedia: {}{} Recuperação{}'.format(amarelo,media,limpar))
