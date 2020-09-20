def leiaint(num):
    num = input(num)
    while True:
        if num.isnumeric():
            break
        else:
            print('Erro!!.Tente novamente!!')
            num = leiaint('Digite um número: ')
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
