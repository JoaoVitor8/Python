valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = valorCasa / (tempo*12)
print(f'Para pagar uma casa de R${valorCasa:.2f} em {tempo} anos, a prestação será de R${prestacao:.2f}')
if prestacao > (salario * 0.3):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo CONCEDIDO!')
