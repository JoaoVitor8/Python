#1-16 Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
# de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = int(input('Quantos m² você ira pintar?: '))
litros = tamanho / 3

if tamanho % 54 == 0:
    latas = tamanho / 54
else:
    latas = (tamanho / 54) + 1

preco = latas * 80
print(f'{latas} de latas')
print(f'R${preco:.2f}')
