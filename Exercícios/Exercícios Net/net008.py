#1-8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês.

gh = float(input('Quanto você ganha por hora?: '))
ht = int(input('Quantas horas você trabalha no mês?: '))

salario = gh * ht

print(f'Meu salario no fim do mês é de {salario}')
