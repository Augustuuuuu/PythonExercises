n = int(input('\033[1;31mPRIMEIRO VALOR: '))
n2 = int(input('\033[1;31mSEGUNDO VALOR: '))
if n > n2:
    print(f'\033[1;97mO PRIMEIRO VALOR É O MAIOR.(\033[1;35m{n}\033[1;97m)')
elif n2 > n:
    print(f'\033[1;97mO SEGUNDO VALOR É O MAIOR. (\033[1;35m{n2}\033[1;97m)')
else:
    print(f'\033[1;97mOS VALORES SÃO IGUAIS. (\033[1;35m{n2}\033[1;97m e \033[1;35m{n}\033[1;97m)')
