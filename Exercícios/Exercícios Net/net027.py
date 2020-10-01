#2-9 Faça um Programa que leia três números e mostre-os em ordem decrescente.

num = []

while True:
    n = int(input('Digite um número: '))
    num.append(n)
    parar = str(input('Quer continuar?: ')).upper().strip()
    if parar == 'N':
        break
    elif parar != 'S':
        print('Erro')
        parar = str(input('Quer continuar?: ')).upper().strip()

num.sort(reverse=True)
print(num)