#2-4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante

letra = str(input('Digite uma letra: ')).upper().strip()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == '0' or letra == 'U':
    print('A letra digitata é uma vogal')
else:
    print('A letra digitada é uma consoante')
