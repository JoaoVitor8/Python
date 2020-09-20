def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade}. Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade}. Voto opcional'
    else:
        return f'Com {idade}. Voto obrigatorio'


nasc = int(input('Em que ano você nascel?: '))
print(voto(nasc))
