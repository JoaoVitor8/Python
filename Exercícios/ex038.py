numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
if numero1 > numero2:
    print('O primeiro número é maior.')
    print(f'{ numero1} é maior que { numero2}.')
elif numero2 > numero1:
    print('O segundo número é maior.')
    print(f'{ numero2} é maior que { numero1}.')
else:
    print(f'Os números são iguais.')
