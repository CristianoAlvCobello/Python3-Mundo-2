maior = 0
menor = 0 
for contagem in range(1,6):
    peso = float(input('Digite o peso da pessoa {}: '.format(contagem)))
    if contagem == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('\nA pessoa mais pesada tem: {}Kg'.format(maior))
print('A pessoa menos pesada tem: {}Kg'.format(menor))
