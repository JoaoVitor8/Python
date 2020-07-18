n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('Como deseja prosseguir?'
                      '\n[ 1 ] somar'
                      '\n[ 2 ] multiplicar'
                      '\n[ 3 ] maior'
                      '\n[ 4 ] novos números'
                      '\n[ 5 ] sair do programa'
                      '\nSua escolha: '))
    if opcao == 1:
        s = n1 + n2
        print('-' * 25)
        print(f'A soma de {n1} + {n2} vale {s}')
        print('-' * 25)
    elif opcao == 2:
        m = n1 * n2
        print('-' * 25)
        print(f'A multiplicação de {n1} x {n2} vale {m}')
        print('-' * 25)
    elif opcao == 3:
        maior = max(n1, n2)
        print('-' * 25)
        print(f'O maior valor digitado foi {maior}')
        print('-' * 25)
    elif opcao == 4:
        print('-' * 25)
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        print('-' * 25)
    elif opcao != 5:
        print('-' * 25)
        print('Opção inválida. Tente novamente.')
        print('-' * 25)
print('Fim')
