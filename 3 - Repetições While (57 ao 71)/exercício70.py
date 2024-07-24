contador = 0
produtomenor = ' '
acimamil = 0
valortotal = 0

while True:
    produto = str(input('Digite o produto: '))
    valor = float(input('Digite seu valor: R$'))

    contador = contador+ 1

    if contador == 1:
        menorvalor = valor
        produtomenor = produto

    if menorvalor > valor:
        menorvalor = valor
        produtomenor = produto
    
    if valor > 1000:
        acimamil += 1
    
    valortotal += valor

    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Quer continuar? ')).strip().lower()
    
    if resposta == 'n':
        break

print(f'\nO total da compra ficou R${valortotal:.2f}')
print(f'O produto com o menor preço foi {produtomenor.capitalize}, que custa R${menorvalor:.2f}')
print(f'Tem {acimamil} produtos que ficam acima dos R$1000')

#Resposta do professor
#if contador == 1 or menorvalor < menor:
#   menorvalor = valor
#   produtomenor = produto
