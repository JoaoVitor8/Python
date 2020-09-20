from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
ano = int(input('Ano de nacimento: '))
cadastro['idade'] = datetime.now().year - ano
cadastro['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['carteira'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - datetime.now().year)

for k, v in cadastro.items():
    print(f'{k} tem {v}')

