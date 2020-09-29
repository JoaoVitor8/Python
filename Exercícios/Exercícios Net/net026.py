#2-8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato

p1 = int(input('Produto um: '))
p2 = int(input('Produto dois: '))
p3 = int(input('Produto trêz: '))

barato = p1

if p2 < p1 and p2 < p3:
    barato = p2
elif p3 < p1 and p3 < p2:
    barato = p3

print(f'O produto mais barato é R${barato}')
