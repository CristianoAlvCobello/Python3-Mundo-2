numero = int(input('Digite um número: '))
contador = numero
resultado = 1

while contador > 1:
    resultado = resultado*contador
    contador = contador-1

print('\nO fatorial do número é: {}'.format(resultado))
