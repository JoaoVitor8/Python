from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
for i, v in enumerate(rank):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} ')
    sleep(1)
