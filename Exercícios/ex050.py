soma = 0
for n in range(1,7):
    numero = int(input('Digite um número:'))
    if numero % 2 == 0:
        soma = soma + numero
print(f'A soma dos pares é = {soma}')
