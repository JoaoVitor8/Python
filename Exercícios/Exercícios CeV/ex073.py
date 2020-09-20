times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco da Gama', 'Atlético-MG', 'Fluminense', 'Botafogo',
         'Ceará SC', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('Ranking:')
contador = 0
for lista_times in times:
    contador += 1
    print(f'{contador}º {lista_times}')
print('5 primeiros colocados:')
lista_5 = times[0:5]
contador = 0
for rank_5 in lista_5:
    contador += 1
    print(f'{contador}º {rank_5}')
print('Os últimos 4 colocados:')
lista_4_ultimos = times[-4:]
contador = 16
for rank_4_ultimos in lista_4_ultimos:
    contador += 1
    print(f'{contador}º {rank_4_ultimos}')
print('Lista de times em ordem alfabética:')
print()
lista_alfabetica = sorted(times)
for rank_alfa in lista_alfabetica:
    print(rank_alfa)
print(f'Posição do time Chapecoence: {times.index("Chapecoense") + 1}ª posição.')
