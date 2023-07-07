import random
from time import sleep
print('\033[1;33m*' * 22)
print('\033[1;97mPEDRA, PAPEL E TESOURA')
print('\033[1;33m*' * 22)
print('\033[1;32mVAMOS JOGAR JOKÊNPO!')
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
sorteio = random.choice(jogadas)
print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
if player.lower() == 'a' and sorteio == 'PAPEL':
    print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 0 A 1')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
elif player.lower() == 'a' and sorteio == 'PEDRA':
    print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 1 A 1')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
elif player.lower() == 'a' and sorteio == 'TESOURA':
    print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 1 A 0')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
elif player.lower() == 'b' and sorteio == 'PAPEL':
    print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 1 A 1')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
elif player.lower() == 'b' and sorteio == 'PEDRA':
    print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 1 A 0')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
elif player.lower() == 'b' and sorteio == 'TESOURA':
    print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 0 A 1')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
elif player.lower() == 'c' and sorteio == 'PEDRA':
    print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 0 A 1')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('0 a 2')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
elif player.lower() == 'c' and sorteio == 'PAPEL':
    print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 1 A 0')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 1')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 0')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
elif player.lower() == 'c' and sorteio == 'TESOURA':
    print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
    sleep(1)
    print(' 1 A 1')
    sleep(1)
    print('\033[1;36mRODADA 2')
    print('\033[1;97mA \033[1;37m: \033[1;33mPEDRA')
    print('\033[1;97mB \033[1;37m: \033[1;32mPAPEL')
    print('\033[1;97mC \033[1;37m: \033[1;31mTESOURA')
    player = str(input('\033[1;97mDIGITE SUA OPÇÃO: '))
    if player.lower() == 'a' and sorteio == 'PAPEL':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'a' and sorteio == 'PEDRA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
    elif player.lower() == 'a' and sorteio == 'TESOURA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'PAPEL':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
    elif player.lower() == 'b' and sorteio == 'PEDRA':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'b' and sorteio == 'TESOURA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'c' and sorteio == 'PEDRA':
        print(f'\033[1;31mVOCÊ PERDEU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('1 a 2')
    elif player.lower() == 'c' and sorteio == 'PAPEL':
        print(f'\033[1;32mVOCÊ GANHOU!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 1')
    elif player.lower() == 'c' and sorteio == 'TESOURA':
        print(f'\033[1;33mEMPATE!\033[1;97m O COMPUTADOR ESCOLHEU {sorteio}')
        print('2 a 2')
print('\033[1;41mFIM\033[m')
