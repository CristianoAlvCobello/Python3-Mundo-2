numero = int(input('Digite um número: '))
resultado = 1

for contador in range(numero, 1, -1):
    resultado = resultado*contador

print('\nO fatorial do número é: {}'.format(resultado))
