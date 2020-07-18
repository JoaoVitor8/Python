from math import fsum
lista_produtos = []
listaprecos = []
produtos1000 = 0
while True:
    produto = str(input("Qual o nome do produto?"))
    lista_produtos.append(produto)
    preco = float(input("Qual o preço do produto?"))
    listaprecos.append(preco)
    if preco > 1000:
        produtos1000 += 1
    continuar = " "
    while continuar not in 'SN':
        continuar = str(input("Adicionar mais produtos?[S/N]")).strip().upper()
    if continuar == 'N':
        break
mais_barato = (lista_produtos[listaprecos.index(min(listaprecos))])
print(f"\nO total gasto na compra foi R${fsum(listaprecos):.2f}")
print(f"{produtos1000} produtos custaram mais de R$1000")
print(f"O produto mais barato é {mais_barato} custando R${min(listaprecos)}\n\n")
