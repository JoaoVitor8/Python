valores = []
while True:
    continuar = ' '
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    if valores.count(valor) == 2:
        print('Valor duplicado! Não vou adicionar...')
        valores.pop()
    else:
        print('Valor adicionado com sucesso...')
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').strip().upper()
    if continuar == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
