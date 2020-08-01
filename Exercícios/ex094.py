cadastro = dict()
pessoas = list()
soma = media = 0
while True:
    cadastro.clear()
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while cadastro['Sexo'] not in 'MF':
        print('ERRO, Por Favor digite apenas M ou F')
        cadastro['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    cadastro['Idade'] = int(input('Idade: '))
    soma += cadastro['Idade']
    pessoas.append(cadastro.copy())
    parar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if parar == 'N':
        break
    while parar not in 'SN':
        print('ERRO, Por Favor digite apenas S ou N')
        parar = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
        if parar == 'N':
            break
print()
print(f'Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'A média de idade é de {media}')
print('As mulheres cadastradas foram: ', end='')
for c in pessoas:
    if c['Sexo'] in 'Ff':
        print(f'{c["Nome"]} ', end='')
print()
print('Pessoas com idade acima da média: ')
for c in pessoas:
    if c['Idade'] >= media:
        print(' ', end=' ')
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
