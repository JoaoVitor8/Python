#2-20 Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
# aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1 = float(input('Nota Um: '))
nota2 = float(input('Nota Dois: '))
nota3 = float(input('Nota Tres: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media < 10:
    print('Aluno Aprovado')
elif media < 7:
    print('Aluno Reprovado')
elif media == 10:
    print('Aprovado com Distinção')
