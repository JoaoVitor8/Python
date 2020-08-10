from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont += p
        print('Fim!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.4)
            cont -= p
        print('Fim!!')
        print('~' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de contar')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
