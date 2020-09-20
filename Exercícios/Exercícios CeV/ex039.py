from datetime import date
genero = int(input('Qual o seu gênero?\n'
               '[1] FEMININO\n'
               '[2] MASCULINO\n'
               '-> '))
if genero == 1:
    print('O alistamento militar não é obrigatório para você.')
elif genero == 2:
    ano = int(input('Digite seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        print('Você tem {} anos e ainda não está na idade de alistamento, '
          'faltam {} anos.\nSeu alistamento será em {}.'.format(idade, 18 - idade, ano + 18))

    elif idade == 18:
        print('Você tem 18 anos. Está na hora de se alistar!')
    else:
        print('Seu tempo de alistamento foi há {} anos.\n'
          'Espero que você tenha se apresentado no ano de {}.'.format(idade - 18, ano + 18))
