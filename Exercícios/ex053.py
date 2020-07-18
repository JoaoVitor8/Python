frase = ''.join(str(input('Diga uma frase: ')).split()).lower()
print('A frase digitada foi:\n{}\nE o contrário dela é:\n{}'.format(frase, ''.join(reversed(frase))))
if ''.join(reversed(frase)) == frase:
    print('Portanto, ela é um palíndromo!')
else:
    print('Portanto, ela não é um palíndromo.')
