#2-2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = int(input('Informe um valor: '))

if n > 0:
    print(f'O valor {n} é positivo')
elif n < 0:
    print(f'O valor {n} é negativo')
else:
    print('Zero é neutro')
