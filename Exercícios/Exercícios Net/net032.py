#2-14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
# calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
# for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input('1° nota: '))
n2 = float(input('2° nota: '))

media = (n1 + n2) / 2

if media > 9:
    n = 'A'
    print('Aprovado')
elif media > 7.5:
    n = 'B'
    print('Aprovado')
elif media > 6:
    n = 'C'
    print('Aprovado')
elif media > 4:
    n = 'D'
    print('Reprovado')
else:
    n = 'E'
    print('Reprovado')

print(f'Sua media foi {media}.')
