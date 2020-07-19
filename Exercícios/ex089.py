ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    parar = str(input('Quer continuar? [S/N] '))
    if parar in 'Nn':
        break

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
