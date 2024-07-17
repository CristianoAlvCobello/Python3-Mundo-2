numero = int(input('Digite um número: '))
divisiveis = 0
for contador in range(1,numero+1):
    if numero%contador == 0:
        print('\033[1;34m', end='')
        divisiveis = divisiveis+1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(contador), end='')
if divisiveis == 2:
    print('\n\033[mÉ primo')
else:
    print('\n\033[mNão é primo')
    