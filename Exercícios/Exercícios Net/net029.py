#2-11 As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o
# reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%

# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Informe seu salário: '))

if salario < 280:
    s = (salario * 20) / 100
    sb = salario + s
    p = 20
elif salario < 700:
    s = (salario * 15) / 100
    sb = salario + s
    p = 15
elif salario < 1500:
    s = (salario * 10) / 100
    sb = salario + s
    p = 10
else:
    s = (salario * 5) / 100
    sb = salario + s
    p = 5

print(f'Seu salário antes do ajuste era de R${salario:.2f}')
print(f'{p}% to seu salário é R${s:.2f}')
print(f'Seu novo salário agora é R${sb:.2f}')
