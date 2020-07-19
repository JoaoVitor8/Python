lista = []
cont = 1
pares = []
impar = []
while True:
    lista.append(int(input(f'Insira o {cont}º valor: ')))
    cont += 1
    resp = str(input('Pretende continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
    for n in range(0, len(lista)):
        if lista[n] % 2 == 0:
            pares.append(lista[n])
        else:
            impar.append((lista[n]))

print(f'QUANTIDADE NÚMEROS DIGITADOS = {len(lista)}')
print(f'NÚMEROS DIGITADOS = {sorted(lista)}')
print(f'NÚMEROS PARES = {pares}')
print(f'NÚMEROS ÍMPARES = {impar}')
