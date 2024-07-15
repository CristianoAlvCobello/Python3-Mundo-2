peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em Metros: '))


imc = peso/altura**2
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
amareloline = '\033[1;4;33m'
limpar = '\033[m'

print('\nSeu IMC é {:.2f} e sua situação é de:'.format(imc), end=' ')
if imc < 18.5:
    print('{}Abaixo do peso{}'.format(vermelho, limpar))

elif imc > 18.5 and imc <= 25:
    print('{}Peso ideal{}'.format(verde,limpar))

elif imc > 25 and imc <= 30:
    print('{}Sobrepeso{}'.format(amarelo,limpar))

elif imc > 30 and imc <= 40:
    print('{}Obesidade{}'.format(amareloline,limpar))

else:
    print('{}Obesidade mórbida{}'.format(vermelho, limpar))
