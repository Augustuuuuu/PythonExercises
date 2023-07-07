a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima PODEM FORMAR um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')
