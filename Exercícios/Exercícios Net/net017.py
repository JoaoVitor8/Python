#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
#pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
#de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
# valores para cima, isto é, considere latas cheias.

import math

area = float(input('tamanho em metros quadrados: '))

litro = area/6  #quantidade de litros
latas18 = (area)/(108)  #quantidade de latas para pintar a área especificada
galao = (area)/(21.6)  #quantidade de galao para pintar a área especificada

if area > 0:  # a area tem que ser maior que zero caso contrario os valores de entradas estão errados.
    preco = math.ceil(latas18)*80
    print('A quantidade de latas de 18 litros a serem compradas é:', math.ceil(latas18), '\nPreço total é de:', preco, 'Reais')
    preco2 = math.ceil(galao)*25
    print('A quantidade de galao de 3.6 litros a serem compradas é', math.ceil(galao), '\nPreço total foi:', preco2)
else:
    print('Dados invalidos')
