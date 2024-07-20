resposta = str(input('Digite um sexo: ')).strip().lower()

while resposta != 'm' and resposta != 'f':
    print('-'*5, '\033[1;31mValor Incorreto\033[m', '-'*5)
    resposta = str(input('Digite um sexo: '))
print('-'*5, '\033[1;32mValor Correto\033[m', '-'*5)

#Resposta do professor
#While resposta not in 'MmFf'
