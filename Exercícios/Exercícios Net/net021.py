#2-3 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Informe seu sexo [F/M]: ')).upper().strip()

if sexo == 'F':
    print('Você informou que é uma mulher')
elif sexo == 'M':
    print('Você informou que é um homem')
else:
    print('Sexo inválido')
