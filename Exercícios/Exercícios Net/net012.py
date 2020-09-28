#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58

a = float(input('Qual sua altura?: '))

peso = (72.7 * a) - 58

print(f'Seu peso ideal é de {peso:.1f}')
