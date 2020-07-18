lista = []
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    lista += [peso]

print(f'O Maior peso foi: {max(lista)}KG')
print(f'O Menor peso foi: {min(lista)}KG')
