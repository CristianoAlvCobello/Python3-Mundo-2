numerousuario = 0
soma = 0
contador = 0

print('Digite 999 para finalizar o programa')
while numerousuario != 999:
    numerousuario = int(input('\nDigite seus números: '))
    contador = contador + 1
    if numerousuario != 999:
        soma = soma + numerousuario
print('\033[1;32mVocê digitou:\033[m {} números'.format(contador-1))
print('\n\033[1;32mA soma de todos números foi:\033[m {}'.format(soma))
