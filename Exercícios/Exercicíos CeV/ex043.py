peso = float(input('Qual o seu peso? (Kg) ').replace(',', '.'))
altura = float(input('Qual a sua altura? (m) ').replace(',', '.'))

imc = peso / (altura ** 2)
ideal_min = 18.5 * (altura ** 2)
ideal_max = 25 * (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f} e você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.1f} e você está no peso certo.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.1f} e você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.1f} e você está com obesidade.')
else:
    print(f'Seu IMC é {imc:.1f} e você está com obesidade mórbida.')

print(f'O seu peso ideal é entre {ideal_min:.1f}Kg e {ideal_max:.1f}Kg.')
