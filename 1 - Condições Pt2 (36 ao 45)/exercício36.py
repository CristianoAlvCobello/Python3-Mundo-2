valorcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos planeja pagar?'))

meses = anos*12
prestacaomensal = valorcasa/meses
salario30 = salario*0.30
verde = '\033[1;32m'
vermelho = '\033[1;31m'
limpar = '\033[m'

print('\nA prestação fica: R${:.2f}'.format(prestacaomensal))
if prestacaomensal < salario30:
    print('\nSeu empréstimo foi {}APROVADO{}'.format(verde,limpar))

else:
    print('\nSeu empréstimo foi {}NEGADO{}'.format(vermelho,limpar))
