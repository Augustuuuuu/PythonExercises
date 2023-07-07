from datetime import date
atual = date.today().year
print('\033[1;31mCONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('\033[1;97mPrecisamos saber qual a data de nascimento do atleta.')
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print(idade)
if idade <= 9:
    print('SUA CATEGORIA É \033[1;36mMIRIM')
elif idade <= 14:
    print('SUA CATEGORIA É \033[1;32mINFANTIL')
elif idade <= 19:
    print('SUA CATEGORIA É \033[1;34mJUNIOR')
elif idade <= 20:
    print('SUA CATEGORIA É \033[1;31mSÊNIOR')
elif idade > 20:
    print('SUA CATEGORIA É \033[1;31mMASTER')
