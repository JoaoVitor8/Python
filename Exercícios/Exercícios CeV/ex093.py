futebol = dict()
partidas = list()
futebol['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {futebol["Nome"]} jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quandos gols na partida {c+1}: ')))
futebol['Gols '] = partidas[:]
futebol['tot'] = sum(partidas)
print()
print()
print(futebol)
print()
print()
for k, v in futebol.items():
    print(f'O campo {k} tem valor {v}.')
print()
print()
print(f'O total foi de {futebol["tot"]} gols')
