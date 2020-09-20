def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}X{comp} é de {a}')


l = float(input('Largura[m]: '))
c = float(input('Comprimento[m]: '))
area(l, c)
