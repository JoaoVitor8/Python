n = int(input('Digite um número [999 para parar]: '))
cont = 0
soma = 0
if n == 999:
    print('Programa finalizado.')
else:
    while n != 999:
        cont += 1
        soma += n
        n = int(input('Digite um número [999 para parar]: '))
    print('A soma dos {} números é {}'.format(cont, soma))
