a = float(input('\033[1;97mDigite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a < b + c and b < a + c and c < b + a:
    print('\033[1;97mOS SEGMENTOS \033[1;32mPODEM\033[1;97m FORMAR UM TRIÂNGULO.', end='')
    if a == b and b == c:
        print('ESSE TRIÂNGULO É UM \033[1;34mEQUILÁTERO.')
    elif a != b != c:
        print('ESSE TRIÂNGULO É UM \033[1;31mESCALENO.')
    else:
        print('ESSE TRIÂNGULO É UM \033[1;35mISÓSCELES.')

else:
    print('\033[1;97mOS SEGMENTOS \033[1;31mNÃO PODEM\033[1;97m FORMAR UM TRIÂNGULO.')
