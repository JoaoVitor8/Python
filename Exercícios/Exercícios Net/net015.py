#1-15 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
#A) salário bruto.
#B) quanto pagou ao INSS.
#C) quanto pagou ao sindicato.
#D) o salário líquido.
#E) calcule os descontos e o salário líquido, conforme a tabela abaixo:

#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

gh = float(input('Quanto você ganha por hora?: '))
ht = int(input('Quantas horas você trabalha no mês?: '))

salariobruto= gh * ht
inss = (salariobruto * 8) / 100
ir = (salariobruto * 11) / 100
sindicato = (salariobruto * 5) / 100
descontos = inss + ir + sindicato
salarioliquido = salariobruto - descontos

print(f'Seu salario bruto é de {salariobruto}')
print(f'Você tera um desconto de R${inss:.2f} de INSS')
print(f'R${ir:.2f} de IR')
print(f'R${sindicato:.2f} para o sindicato')
print(f'E seu salario liquido será de R${salarioliquido:.2f}')
