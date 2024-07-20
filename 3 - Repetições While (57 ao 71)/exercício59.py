numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
resposta = 0
solicitado = ''
instruções = str("""
(1) Somar
(2) Multiplicar
(3) Maior
(4) Novos números
(5) Sair do programa

Digite aqui: """)

while resposta != 5:
    resposta = int(input((instruções)))
    
    if resposta == 1:
        resultado = numero1+numero2
        solicitado = 'Somar'
    
    elif resposta == 2:
        resultado = numero1*numero2
        solicitado = 'Multiplicar'

    elif resposta == 3:
        if numero1 > numero2:
            resultado = numero1
        else:
            resultado = numero2
        solicitado = 'Maior'
    
    elif resposta == 4:
        numero1 = int(input('Digite o número 1 novo: '))
        numero2 = int(input('Digite o número 2 novo: '))
        resultado = str('Novos números, {} e {}'.format(numero1,numero2))
        solicitado = 'Novos números'
    
    elif resposta == 5:
        resultado = str('\033[1;31mFim do programa\033[m')
        solicitado = str('Sair do programa')

    print('\n\033[1;32mSolicitado:\033[m {}'.format(solicitado))
    print('\033[1;36mResultado:\033[m {}'.format(resultado))
