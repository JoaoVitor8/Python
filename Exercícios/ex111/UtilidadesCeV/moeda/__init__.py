def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print(f'Preço em Analize:       \t{moeda(preco)}')
    print(f'Dobro do preço:         \t{dobro(preco, True)}')
    print(f'Metade do preço:        \t{metade(preco, True)}')
    print(f'Preço aumentado em {taxaa}%: \t{aumentar(preco, taxaa, True)}')
    print(f'Preço diminuido em {taxar}%: \t{diminuir(preco, taxar, True)}')
