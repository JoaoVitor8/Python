from datetime import date
atual = date.today().year
contma = 0
contmn = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = atual - nasc
    if idade > 21:
        contma += 1
    else:
        contmn += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(contma))
print('E também tivemos {} pessoas menores de idade'.format(contmn))
