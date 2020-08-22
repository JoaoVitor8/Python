from ex111.UtilidadesCeV import moeda
from ex111.UtilidadesCeV import dados


p = dados.leiaDinheiro('Digite um preço: R$')
moeda.resumo(p, 17, 30)
