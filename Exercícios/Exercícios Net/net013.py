#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#A) Para homens: (72.7*h) - 58
#B) Para mulheres: (62.1*h) - 44.7

s = str(input('Qual seu sexo?[M/F]: ')).upper().strip()
h = float(input('Qual sua altura?: '))

if s == 'M':
    ph = (72.7 * h) - 58
    print(f'O peso ideal de um homem com {h} de altura é {ph:.1f}kg')
elif s == 'F':
    pm = (62.1 * h) - 44.7
    print(f'O peso ideal de uma mulher com {h} de altura é {pm:.1f}')
