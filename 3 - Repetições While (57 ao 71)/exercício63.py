contadorusuario = int(input('Digite um número: '))

numero = 0
numeroanterior = 1
contador = 0
fibonacci = 0

print('0')
while contador < contadorusuario-1:
    resultado = numero+numeroanterior
    numeroanterior = fibonacci-numero
    fibonacci = resultado+numeroanterior
    contador = contador + 1
    print(fibonacci)
 