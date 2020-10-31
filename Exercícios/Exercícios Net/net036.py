#2-18 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('Informe uma data abaixo')
dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

if dia <= 30 and mes <= 12 and ano >= 1:
    print(f'A data {dia}/{mes}/{ano} é valida')
else:
    print(f'A data {dia}/{mes}/{ano} é invalida')
