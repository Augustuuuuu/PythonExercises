'''print('Desafio 018')
import trigonometry
num = float(input('Digite o valor de seu angulo: '))
seno = trigonometry.sin_ang(num)
cosseno = trigonometry.cos_ang(num)
tangente = trigonometry.tan_ang(num)
print(f'O cosseno é {cosseno}')
print(f'O seno é {seno}')
print(f'A tangente é {tangente}')'''

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo: '))
seno = sin(radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
cos = cos(radians(an))
print(f'O ângulo de {an} tem o COSSENO de {cos:.2f}')
tan = tan(radians(an))
print(f'O ângulo de {an} tem a TANGENTE de {tan:.2f}')
