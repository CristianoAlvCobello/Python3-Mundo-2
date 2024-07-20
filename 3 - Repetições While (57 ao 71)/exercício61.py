primeirotermo = int(input('Digite o 1º termo da progessão: '))
razao = int(input('Digite a razão da progressão: '))
contador = 0

while contador < 10:
    contador = contador+1
    termo = contador
    termo = primeirotermo+razao*(termo-1)
    print(termo)

#Resposta do professor
#termo = primeirotermo
#termo = termo + razao
