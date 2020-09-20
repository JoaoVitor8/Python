while True:
    n1 = int(input('Quer ver a tabuada de qual valor? '))
    if n1 < 0:
        print('PROGAMA DE TABUADA ENCERRADO.')
        break
    for c in range(1, 10):
        c += 1
        m = n1 * c
        print(f'{n1} x {c} = {m}')
