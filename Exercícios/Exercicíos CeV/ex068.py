from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
cont = 0
while True:
    pc=randint(0, 10)
    jog=int(input('Digite um valor de 0-10: '))
    while jog < 0 or jog > 10:
        jog = int(input('Tente Novamente. Apenas valores de 0-10: '))
    poi=input('Par ou Ímpar?[P/I] ').upper()[0]
    while poi not in 'PpIi':
        poi = input('Valor Inválido! Digita apenas P ou I: ')

    soma = pc + jog
    print(f'Você jogou {jog} e o computador jogou {pc}. Total de {soma} deu', end=' ')
    if soma % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR.')

    if poi in 'Pp' and soma % 2 == 0 or poi in 'Ii' and soma % 2 != 0:
        print('VOCÊ VENCEU!')
        cont += 1
    else:
        print('VOCÊ PERDEU!')
        break

print('FIM DE JOGO.', end=' ')
if cont == 1:
    print(f'Você venceu {cont} vez')
elif cont > 1:
    print(f'Você venceu {cont} vezes')
else:
    print('Você não acertou nenhuma!')
