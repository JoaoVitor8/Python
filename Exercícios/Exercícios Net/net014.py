#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda
# vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João
# deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = int(input('Quanto pesa seu peixe?: '))

if peso > 50:
    for c in range(50, peso):
        c += 1
        menos = c - 50
        multa = menos * 4
    print(f'Devido ao regulamento de pesca do estado SP você deve pagar uma multa de R$4,00 por quilo excedente\n'
          f'Sua multa será de {multa}.O quilo excedente foi de {menos}Kg')
elif peso <= 50:
    print('Seu peixe não ultrapassol 50Kg, você não terá que pagar multa!')
