aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] <= 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Recuperação'

print()

print(f'O nome é igual a {aluno["Nome"]}')
print(f'A média é igual a {aluno["Média"]}')
print(f'Situação: {aluno["Situação"]}')
