print('\033[1;97mIMC')
altura = float(input('\033[1;32mSUA ALTURA: '))
peso = float(input('\033[1;32mSEU PESO: \033[1;97m'))
imc = peso / (altura * altura)
print(F'Seu IMC é {imc:.2f}.')
if imc < 18.5:
    print('Você está \033[1;35mabaixo do peso.')
elif imc < 25:
    print('Você está no peso \033[1;34mideal.')
elif imc < 30:
    print('Você está com \033[1;31msobrepeso.')
elif imc < 40:
    print('Você está \033[1;31mobeso.')
else:
    print('Você está com \033[1;31mOBESIDADE MORBIDA.')
