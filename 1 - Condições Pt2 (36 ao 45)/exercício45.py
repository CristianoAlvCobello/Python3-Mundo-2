from random import choice

usuario = input('pedra, pepel ou tesoura: ').strip().lower()

jokenpo = ['pedra', 'papel', 'tesoura']
maquina = choice(jokenpo)
vermelho = '\n\033[1;31m'
verde = '\n\033[1;32m'
roxo = '\n\033[35m'
limpar = '\033[m'

if usuario == 'pedra' or usuario == 'papel' or usuario == 'tesoura':
   print('Sua resposta: {}'.format(usuario))
   print('Resposta da maquina: {}'.format(maquina))
   print(end='')
   
   if (maquina == 'pedra' and usuario == 'tesoura') or (maquina == 'papel' and usuario == 'pedra') or (maquina == 'tesoura' and usuario == 'papel'):
      print('{}VOCÊ PERDEU{}'.format(vermelho,limpar))
      
   elif maquina == usuario:
      print('{}EMPATE{}'.format(roxo,limpar))
   
   else:
      print('{}VOCÊ GANHOU{}'.format(verde,limpar))

else: 
   print('Opção inválida')
