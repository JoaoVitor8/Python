prod = float(input('Qual o preço do produto: R$'))
print(f'O produto que custava R${prod}, na promoção de desconto de 5%, passará custar R${prod - (prod * 5 /100):.2f}')
