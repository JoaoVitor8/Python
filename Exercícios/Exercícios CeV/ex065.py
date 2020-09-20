numero = frase = contador = soma = 0
lista = []
while frase != "N":
    numero = int(input("Digite um número: "))
    frase = str(input("Quer continuar?[S/N]: ")).upper().strip()[0]
    contador += 1
    soma += numero
    lista.append(numero)
media = soma / contador
maior = max(lista)
menor = min(lista)
print(f"Foram contados {contador} números e a média entre eles é de {media}")
print(f"O maior valor foi {maior} e o menor {menor}")
