primeirotermo = int(input('Digite o 1º termo da progessão: '))
razao = int(input('Digite qual a razão da progressão: '))
termo = 0

for contador in range(1, 11):
    termo = contador
    termo = primeirotermo+razao*(termo-1)
    print('\033[1;34m',termo,'\033[m', end=' -> ')
print('fim')