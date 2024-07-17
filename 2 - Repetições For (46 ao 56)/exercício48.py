soma = 0
numeros = 0

for contador in (range(1, 501)):
    if contador%3 == 0 and contador%2 != 0:
        soma = soma+contador
        numeros = numeros+1
print('A soma dos {} números encontrados foi {}'.format(numeros, soma))
