def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro!! Por Favor Digite um número inteiro valido')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por Favor Digite um número real valido')
            continue
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
