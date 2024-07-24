contador = 0

while True:
    numero = int(input('Digite um número positivo: '))
    if numero < 0:
        break
    print('-'*20)
    while numero and contador < 10:
        contador = contador+1
        tabuada = numero*contador
        print(f'{numero} x {contador} = {tabuada}')
    contador = 0
    print('-'*20)
print('\nObrigado por usar este programa, volte sempre')
