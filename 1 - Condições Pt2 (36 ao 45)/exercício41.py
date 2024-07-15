from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))

idade = date.today().year-nascimento

if idade <= 9:
    print('\n\033[1;36mMirim\033[m')

elif  idade > 9 and idade <= 14:
    print('\n\033[1;32mInfantil\033[m')

elif idade > 14 and idade <= 19:
    print('\n\033[1;35mJunior\033[m')

elif idade <= 25:
    print('\n\033[1;31mSênior\033[m')

else:
    print('\n\033[1;7mMaster\033[m')
