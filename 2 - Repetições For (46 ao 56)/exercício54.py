from datetime import date
maioridade = 0
menoridade = 0

for contagem in range(1,8):
    nascimento = int(input('Digite nascimento da pessoa {}: '.format(contagem)))
    idade = date.today().year-nascimento
    if idade >= 18:
        maioridade = maioridade+1
    else:
        menoridade = menoridade+1

print('Quantidade de pessoas da maioridade: {}'.format(maioridade))
print('Quantidade de pessoas da menoridade: {}'.format(menoridade))
