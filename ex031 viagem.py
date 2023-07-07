n = float(input('Digite a distância da sua viagem em km: '))
if n <= 200:
    print(f'Sua viagem irá custar R${n * 0.50:.2f}.')
else:
    print(f'Sua viagem custará R${n * 0.45:.2f}')
x = n * 0.50 if n <= 200 else n * 0.45
print(f'A sua passagem custará R${x:.2f}')
