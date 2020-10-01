#2-12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
# descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20%

#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00

vh = int(input('Quanto você ganha por hora?: '))
ht = int(input('Quantas horas você trabalha por mês?: '))

sb = vh * ht
fgts = (sb * 11) / 100
inss = (sb * 10) / 100

if sb < 900:
    ir = 0
elif sb < 1500:
    ir = (sb * 5) / 100
elif sb < 2500:
    ir = (sb * 10) / 100
else:
    ir = (sb * 20) / 100

td = ir + inss
sl = sb - td

print(f'Salario Bruto: R${sb:.2f}')
print(f'IR: R${ir:.2f}')
print(f'INSS: R${inss:.2f}')
print(f'FGTS: R${fgts:.2f}')
print(f'Total de Descontos: R${td:.2f}')
print(f'Salário liquido: R${sl:.2f}')
