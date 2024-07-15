from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))

idade = date.today().year-nascimento

verde = '\n\033[1;32m'
vermelho = '\n\033[1;31m'
ciano = '\n\033[1;36m'
limpar = '\033[m'

if  idade > 18:
    tempopassado = idade-18
    anoalistar = date.today().year-tempopassado
    print('{}Já passou o tempo de se alistar, faz {} ano(s), seu alistamento foi em {}{}'.format(vermelho,tempopassado,anoalistar,limpar))

elif idade < 18:
    tempofaltando = (idade-18)*-1
    anoalistar = date.today().year+tempofaltando
    print('{}Ainda não precisa se alistar, falta {} ano(s), seu alistamento é em {}{}'.format(ciano,tempofaltando,anoalistar,limpar))

else:
    print('{}Está na hora de se alistar{}'.format(verde, limpar))
 