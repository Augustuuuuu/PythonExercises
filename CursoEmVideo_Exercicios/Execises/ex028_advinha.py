from random import randint
from time import sleep
s = [0, 1, 2, 3, 4, 5]
r = randint(0, 5)
print('====' * 17)
print('Estou pensando em um número de 0 a 5. Advinhe qual número pensei.')
print('====' * 17)
n = int(input('Digite um valor: '))
print('PROCESSANDO...')
sleep(3)
if n == r:
    print('VOCÊ ACERTOU!!!')
else:
    print('VOCÊ ERROU, TENTE NOVAMENTE.')
print(f'Eu pensei em {r}')
