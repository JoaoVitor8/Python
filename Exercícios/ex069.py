maior = homen = mulher = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    cont = str(input('Desja Continuar[S/N] :')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homen += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if cont == 'N':
        break
print(f'Das pessoas cadastradas \n  {maior} tem mais de 18 anos \n '
      f' {homen} Homens foram cadastrados \n  {mulher} Mulheres tem menos de 20 anos')
