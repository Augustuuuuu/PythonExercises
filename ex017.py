'''print('Desafio 017')
import math
num = float(input('Digite o valor do cateto oposto: '))
num2 = float(input('Digite o valor do cateto adjacente: '))
v1 = math.pow(num, 2)
v2 = math.pow(num2, 2)
print(f'O valor ao quadrado dos catetos resulto em: {v1} e {v2}')
soma = (v1+v2)
resultado = math.sqrt(soma)
print(f'A hipotenusa equivale a {resultado:.2f}')'''
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o catato adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa será {hi:.2f}')
