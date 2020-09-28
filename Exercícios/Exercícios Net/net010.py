#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
#     C = 5 * ((F-32) / 9).

tc = float(input('Informe uma temperatura em Celsius: '))

f = (tc * 9/5) + 32

print(f'A temperatura de Celsius é de {f}°C')
