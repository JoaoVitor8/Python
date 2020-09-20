a1 = int(input('Informe o 1° termo da PA: '))
razao = int(input('Informe a razao da PA: '))
count = total = 0
termos = 10

while termos != 0:
    total += termos
    while count < total:
        print(a1, end=' ')
        count += 1
        a1 += razao
    print()
    termos = int(input('Quantos novos termos vc quer? [Digite 0 para encerrar] '))
print(f'FIM! O programa foi finalizado com {total} termos!!')
