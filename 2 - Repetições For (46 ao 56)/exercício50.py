pares=0

for contador in (range(0,6)):
    numeros = int(input('Digite um número: '))
    if numeros%2 == 0:   
        pares = pares+numeros
print('\nA soma apenas de números PARES é: \033[1;34m{}\033[m'.format(pares))
