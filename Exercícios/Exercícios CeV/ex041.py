from datetime import date
nasc = int(input('Digite o ano de nascimento do Atleta: ').strip())
idade = date.today().year - nasc

mirim = range(0, 10)
infatil = range(10, 15)
junior = range(15, 20)
senior = 20

if idade in mirim:
    print(f'MIRIM. O Atleta tem {idade} anos, então se encaixa nessa categoria.')
elif idade in infatil:
    print(f'INFANTIL. O Atleta tem {idade} anos, então se encaixa nessa categoria.')
elif idade in junior:
    print(f'JUNIOR. O Atleta tem {idade} anos, então se encaixa nessa categoria.')
elif idade == senior:
    print(f'SENIOR. O Atleta tem {idade} anos, então se encaixa nessa categoria.')
else:
    print(f'MASTER. O Atleta tem {idade} anos, então se encaixa nessa categoria.')
