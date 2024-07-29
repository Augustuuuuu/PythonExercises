print('\033[1;97mCONVERSÃO DE NÚMEROS')
n = int(input('Digite um número inteiro qualquer: '))
print('Conversão de inteiro para binário, octal ou hexadecimal.')
print('Digite \033[1;31m1\033[1;97m para binário, \033[1;31m2\033[1;97m '
      'para octal e \033[1;31m3\033[1;97m para hexadecimal.')
c = int(input('Digite aqui: '))
if c == 1:
    bin = (bin(n)[2:])
    print(bin)
elif c == 2:
    octal = (oct(n)[2:])
    print(octal)
elif c == 3:
    hexa = (hex(n)[2:])
    print(hexa)
else:
    print('Opção invalida.')