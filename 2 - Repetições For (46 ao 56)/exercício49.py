numero = int(input('Digite um número: '))

for tabuada in (range(1, 11)):
    resultado = numero*tabuada
    print('{} x {} = {}'.format(numero,tabuada,resultado))
