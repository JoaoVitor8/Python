#1-11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#A) O produto do dobro do primeiro com metade do segundo .
#B) A soma do triplo do primeiro com o terceiro.
#C) O terceiro elevado ao cubo.


ni1 = int(input('Digite um número inteiro: '))
ni2 = int(input('Digite outro número inteiro: '))
nr = float(input('Digite um número real: '))

produto = (ni1 * 2) * (ni2 / 2)
soma = (ni1 * 3) + nr
cubo = nr ** 3

print(f'O produto do dobro do primeiro com metade do segundo é {produto}')
print(f'A soma do triplo do primeiro com o terceiro é {soma}')
print(f'O terceiro elevado ao cubo é {cubo}')
