#1-9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#     C = 5 * ((F-32) / 9).

tf = float(input('Informe uma temperatura em Fahrenheit: '))

c = 5 * ((tf - 32) / 9)

print(f'A temperatura de Celsius é de {c}°C')
