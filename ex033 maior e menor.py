n = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
n2 = int(input('Digite outro número: '))
if n > n1 > n2:
    print(f'O maior valor é: {n}')
if n1 > n2 > n:
    print(f'O maior valor é: {n1}')
if n2 > n1 > n:
    print(f'O maior valor é: {n2}')
if n2 < n1 < n:
    print(f'O menor valor é: {n2}')
if n1 < n2 < n:
    print(f'O menor valor é: {n1}')
if n < n1 < n2:
    print(f'O menor valor é: {n}')
