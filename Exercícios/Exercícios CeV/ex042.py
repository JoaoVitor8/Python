n = float(input('Digite o comprimento do primeiro lado :'))
n2 = float(input('Digite o comprimento do segundo lado :'))
n3 = float(input('Digite o comprimento do terceiro lado :'))
if n <= n2 + n3 and n2 <= n+n3 and n3 <= n + n2:
    print('Há possibilidade de formar um triangulo ', end='')
    if n== n2 == n3:
        print('\033[4;34mEquilatero\033[m')
    elif n != n2 != n3 != n:
        print('\033[4;35mEscaleno\033[m')
    else:
        print('\033[4;36mIsosceles\033[m')
else:
    print('Não a possibilidade de formar um triangulo!')
