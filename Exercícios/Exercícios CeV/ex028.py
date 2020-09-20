from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
jogador = int(input('Digite um número entre 0 e 5 : '))
sleep(1.5)
if computador == jogador:
    print(f'Você acertou! escolhi o número {jogador}')
else:
    print(f"Você errou! O número correto era {computador} e não {jogador}")
