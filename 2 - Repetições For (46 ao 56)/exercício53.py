frase = str(input('Digite uma frase: ')).strip().lower()

palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = ''

for letra in range(len(tudojunto)-1,-1,-1):
    inverso = inverso + tudojunto[letra]

if inverso == tudojunto:
    print('\n\033[1;32mÉ um palindromo\033[m')

else:
    print('\n\033[1;31mNão é um palindromo\033[m')
