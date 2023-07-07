print('\033[1;97mBANCO')
print('\033[1;31mEmpréstimo bancário\033[1;97m')
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
ano = int(input('Digite a quantidade de anos em que você deseja pagar: '))
emprestimo = casa / (ano * 12)
print(f'Para comprar uma casa de \033[1;32mR$\033[1;37m{casa:.2f}\033[1;97m com \033[1;32mR$\033[1;37m{salario:.2f} '
      f'\033[1;97m de salário você precisará de pagar \033[1;32mR$\033[1;37m{emprestimo:.2f}\033[1;97m em emprestimo '
      f' mensal.')
if emprestimo <= salario * 30 / 100:
    print('\033[1;32mEMPRESTIMO APROVADO.')
else:
    print('\033[1;31mEMPRESTIMO NEGADO.')