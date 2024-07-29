n = int(input('Digite um número de 1 a 10000: '))
resultado = n % 2
if resultado == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é impar.')
