resposta = 's'
contador = 0
soma = 0
maior = 0
menor = 0

while resposta == 's':
    numero = int(input('Digite o número: '))
    resposta = str(input('Quer mais(s/n)? '))
    contador = contador+1
    
    soma = soma+numero

    if contador == 1:
        maior = numero
        menor = numero
    
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

media = soma/contador
print('\n\033[1;32mA média foi:\033[m {}'.format(media))
print('\033[1;32mO menor valor foi:\033[m {}'.format(menor))
print('\033[1;32mO maior valor foi:\033[m {}'.format(maior))
    