#2-17 Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não
# bissexto.

ano = int(input('Verifique se um ano é Bissexto: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é Bissexto')
else:
    print('Esse ano não é Bissexto')
