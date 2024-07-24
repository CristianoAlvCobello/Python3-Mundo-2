soma = 0
contador = 0

while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        break
    contador = contador + 1
    soma = soma+numero
print(f'A soma de todos os {contador} números foi {soma}')
