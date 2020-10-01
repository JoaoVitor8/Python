#2-13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
# digitar outro valor deve aparecer valor inválido.

semana = ('0', 'Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')

n = int(input('Digite um número da semana que NÃO seja ZERO: '))

while True:
    if n <= 7:
        print(semana[n])
        break
    else:
        print('Valor invalido, tente novamnete')
        n = int(input('Digite um número da semana que NÃO seja ZERO: '))
