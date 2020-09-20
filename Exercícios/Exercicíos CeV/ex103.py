def ficha(num='Desconhecido', gol=0):
    print(f'O jogador {num} fez {g} gol(s) no compeonado.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
