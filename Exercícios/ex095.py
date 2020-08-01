jogadores = list()
futebol = dict()
partidas = list()
while True:
    futebol.clear()
    futebol['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {futebol["Nome"]} jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quandos gols na partida {c+1}: ')))
    futebol['Gols'] = partidas[:]
    futebol['tot'] = sum(partidas)
    jogadores.append(futebol.copy())
    parar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if parar == 'N':
        break
    while parar not in 'SN':
        print('ERRO, Por Favor digite apenas S ou N')
        parar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
        if parar == 'N':
            break
print()
for i in futebol.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar fixa de qual jogador?: [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Erro, Não existe o jogador {busca}')
    else:
        print(f'Verificando jogador {jogadores[busca]["Nome"]}')
        for i, g in enumerate(jogadores[busca]['Gols']):
            print(f'No jogo {i+1} fez {g} Gols')
print()
