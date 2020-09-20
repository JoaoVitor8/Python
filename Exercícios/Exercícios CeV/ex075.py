tupla = tuple(int(input('Digite valor: '))for c in range(4))
print(f'Sua tupla ficou assim: {tupla}.')
contnove = 0
npares = (0,)
for numrevelado in tupla:
    if numrevelado == 9:
        contnove += 1
    if numrevelado % 2 == 0 and numrevelado != 0:
        par = (numrevelado,)
        npares = npares + par
print(f'O 1º TRÊS está na posição {tupla.index(3)}.' if numrevelado == 3 else ('Não há 3 nesta tupla.'))
print(f'O número 9 apareceu {contnove}x na tupla.' if contnove > 0 else ('Não há 9 nesta tupla.'))
print(f'São pares: {str(npares[1:]).strip("(,)")}.' if len(str(npares)) > 4 else ('Não há números pares.'))

