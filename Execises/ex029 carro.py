v = float(input('Digite a velocidade em que o carro estava: '))
if v <= 80.90:
    print('Você está dentro da lei. Parabéns')
else:
    print('Você está multado!')
    n = v - 80
    m = n * 7
    print(f'Sua multa é de R${m:.2f}')
