maisvelho = 0
todasidades = 0
nomemaisvelho = ''
menosde20 = 0

for contagem in range(1,5):
    print('-'*5, '{}ª PESSOA'.format(contagem), '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().lower()
    
    todasidades = todasidades + idade

    if sexo == 'm' and idade > maisvelho:
        nomemaisvelho = nome
        maisvelho = idade

    elif sexo == 'f' and idade < 20:
        menosde20 = menosde20 + 1

media = todasidades/contagem

print('\nA média do grupo é: {} anos'.format(media))
print('O nome do homem mais velho: {}, {} anos'.format(nomemaisvelho.capitalize(), maisvelho))
print('Mulheres com menos de 20 anos: {}'.format(menosde20))
