nome = str(input('Digite uma palavra: ')).strip().upper().replace(' ',"").replace('Á',"A")
print(f"A letra A na frase digitada aparece {nome.count('A')} vezes")
print(f"A primeira letra A aparece na posição {(nome.find('A')+1)}")
print(f"A última letra A aparece na posição {(nome.rfind('A')+1)}")
