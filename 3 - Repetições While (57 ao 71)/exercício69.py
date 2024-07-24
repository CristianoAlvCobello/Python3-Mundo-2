maiorde18 = 0
homens = 0
mulher = 0

while True:
    idade = int(input('\nDigite a idade: '))
    sexo = ' '

    while sexo not in 'mf':
        sexo = str(input('Digite o sexo(m/f): ')).strip().lower()
    
    if idade > 18:
        maiorde18 += 1
    
    if sexo == 'm':
        homens += 1
    
    if sexo == 'f' and idade < 20:
        mulher += 1
    
    resposta = ' '
    while resposta not in 'sn':
        resposta = str(input('Quer cadastrar mais(s/n)? ')).strip().lower()

    if resposta == 'n':
        break

print(f'\nQuantidade de mulheres com menos de 20 anos: {mulher}')
print(f'Pessoas com mais de 18 anos: {maiorde18}')
print(f'Quantidade de homens: {homens}')
