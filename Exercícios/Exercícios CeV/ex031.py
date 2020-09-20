km = float(input('Qual a distância em (Km) você deseja percorrer? '))
if km <= 200:
    print(f'Sua passagem vai custar {km * 0.5} reais. ')
else:
    print(f'Sua passagem vai custar {km * 0.45} reais. ')
