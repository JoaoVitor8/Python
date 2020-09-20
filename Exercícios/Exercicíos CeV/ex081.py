lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar?[S/N] ').upper().strip()[0]
    if resp in 'N':
        break
print('=' * 40, f'\nVocê digitou{len(lista)} números.')
print(f'Os valores em ordem decrescente são {sorted(lista, reverse = True)}')
print('O número 5 aparece na lista!' if 5 in lista else 'o número 5 não aparece na lista!')
