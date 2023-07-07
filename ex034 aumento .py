s = float(input('Digite seu salário: '))
aumento = s * 10 / 100
aumento2 = s * 15 / 100
if s > 1250:
    print(f'Você recebeu um aumento de 10%, agora receberá {aumento + s}')
else:
    print(f'Você recebeu um aumento de 15%, agora receberá {aumento2 + s}')
