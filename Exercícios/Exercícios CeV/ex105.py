def notas(*n, sit=False):
    '''

    :param n: Notas indicadas
    :param sit: situação(Opcional)
    :return: retorno do valor
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['media'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r


res = notas(10.0, 10.0)
print(res)
