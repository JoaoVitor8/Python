base = int(input('Número inteiro para conversão: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL ')
opcao = int(input('Sua opção: '))
n1 = bin(base)
n2 = oct(base)
n3 = hex(base)
if opcao == 1:
    print(f'{base} convertido para BINÁRIO é igual a {n1[2:]}')
elif opcao == 2:
    print(f'{base} convertido para OCTAL é igual a {n2[2:]}')
elif opcao == 3:
    print(f'{base} convertido para HEXADECIMAL é igual a {n3[2:]}')
else:
    print('Não existe esta opção')
