valor = float(input('Digite o valor do produto: R$'))
pagamento = int(input("""
1 - Cartão 3x ou mais, 20% De juros
2 - Cartão 2x, Preço normal
3 - Á vista (Cartão), 5% Desconto
4 - Á vista (Dinheiro/Cheque), 10% Desconto
                      
Qual a forma de pagamento? """))

if pagamento == 1:
    meses = int(input('Quantas vezes no Cartão? '))
    juros = valor*0.20
    valorfinal = valor+juros
    parcela = valor/meses
    print('\n\033[1;32mEm {}x de R${}, COM JUROS\033[m'.format(valorfinal,parcela))

elif pagamento == 2:
    valorfinal = valor
    parcela = valor/2
    print('\n\033[1;32mEm 2x de R${}, SEM JUROS\033[m'.format(parcela))

elif pagamento == 3:
    valorfinal = valor-(valor*0.05)

elif pagamento == 4:
    valorfinal = valor-(valor*0.10)

else:
    print('Opção inválida')

print('\n\033[1;32mO valor final do produto: R${}\033[m'.format(valorfinal))
