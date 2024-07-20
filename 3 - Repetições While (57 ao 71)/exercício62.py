primeirotermo = int(input('Digite o 1º termo da progessão: '))
razao = int(input('Digite a razão da progressão: '))
contador = 0
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador < total:
        contador = contador+1
        termo = contador
        termo = primeirotermo+razao*(termo-1)
        print(termo, end=' ')
    mais = int(input('\nQuer mais? '))
print('\nForam {} termos apresentador'.format(total))
print('\n\033[1;31mFim\033[m')
