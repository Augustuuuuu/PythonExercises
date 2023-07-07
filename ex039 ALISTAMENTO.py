from datetime import date
print('\033[1;32mALISTAMENTO')
ano = date.today().year
nasc = int(input('\033[1;97mDigite o ano em que seu filho nasceu: '))
idade = ano - nasc
print(f'Quem nasceu em {nasc} hoje tem {idade} anos.')
if idade == 18:
    print('\033[1;32mESTÁ NA HORA DE SE ALISTAR!')
elif idade > 18:
    restante = idade - 18
    print('\033[1;33mJÁ PASSOU DA HORA!')
    print(f'\033[1;97mPASSARAM-SE {restante} ANOS DO TEMPO CERTO!')
    print(f'Você deveria ter se alistado em {ano - restante}')
elif idade < 18:
    print('\033[1;31mNÃO ESTÁ NA HORA!')
    restante = 18 - idade
    print(f'\033[1;97mFaltam {restante} anos para chegar lá!')
    print(f'Você só se alistará em {ano + restante}')