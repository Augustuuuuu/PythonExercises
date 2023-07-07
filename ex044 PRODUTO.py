print('\033[1;97mCALCULADOR DE PREÇO')
valor = float(input('\033[1;33mPREÇO: \033[1;97m'))
ad = valor * 10 / 100
ac = valor * 5 / 100
ate2 = valor
x = valor * 20 / 100
print('Temos opções de pagamento.')
print()
print('1: À vista dinheiro/cheque: 10% de desconto.')
print('2: À vista no cartão: 5% de desconto.')
print('3: Em até 2x no cartão: preço normal')
print('4: 3x ou mais no cartão: 20% de juros.')
opcao = int(input('Digite qual opção você quer: '))
if opcao == 1:
    print(f'O valor fica \033[1;31m{valor - ad:.2f}')
elif opcao == 2:
    print(f'O valor fica \033[1;31m{valor - ac:.2f}')
elif opcao == 3:
    parcela = valor / 2
    print(f'\033[1;97mVocê ira pagar 2 parcelas de R$\033[1;31m{parcela:.2f}')
elif opcao == 4:
    print(f'O valor total ficará R$\033[1;31m{valor + x:.2f}')
    qparcela = int(input('\033[1;97mQuantas parcelas? '))
    if qparcela >= 13:
        print('Quantia de parcelas invalidas. Só passamos parcelas de 3 até 12 vezes.')
    elif qparcela >= 3:
        valor2 = valor + x
        print(f'Você ira pagar parcelas de R$\033[1;31m{valor2 / qparcela:.2f}')
else:
    print('Opção invalida')
