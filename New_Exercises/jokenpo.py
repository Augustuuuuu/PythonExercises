import random
print("JOKENPO")
print("Escolha uma das opções")
print("===" * 10)
print("1 : Pedra")
print("2 : Papel")
print("3 : Tesoura")
print("===" * 10)

computador = 0
jogador = 0
while computador != 2 or jogador != 2:
    escolha_computador = random.randint(1,3)
    escolha = int(input(" "))
    while escolha > 3 or escolha <= 0:
        print("Digite uma opção válida! 1, 2 ou 3\n")
        escolha = int(input(""))
    if escolha == escolha_computador:
        print("Empate!")
    elif escolha == 1 and escolha_computador == 2:
        computador += 1
        print(f"Computador escolheu Papel! {computador} ponto(s) para o computador.")
        print(f"Placar: Computador {computador} x {jogador} Você")
    elif escolha == 1 and escolha_computador == 3:
        jogador += 1
        print(f"Computador escolheu Tesoura! {jogador} ponto(s) para você.")
        print(f"Placar: Computador {computador} x {jogador} Você")
    elif escolha == 2 and escolha_computador == 1:
        jogador += 1
        print(f"Computador escolheu Pedra! {jogador} ponto(s) para você.")
        print(f"Placar: Computador {computador} x {jogador} Você")
    elif escolha == 2 and escolha_computador == 3:
        computador += 1
        print(f"Computador escolheu Tesoura! {computador} ponto(s) para o computador.")
        print(f"Placar: Computador {computador} x {jogador} Você")
    elif escolha == 3 and escolha_computador == 1:
        computador += 1
        print(f"Computador escolheu Pedra! {computador} ponto(s) para o computador.")
        print(f"Placar: Computador {computador} x {jogador} Você")
    elif escolha == 3 and escolha_computador == 2:
        jogador += 1
        print(f"Computador escolheu Papel! {jogador} ponto(s) para você.")
        print(f"Placar: Computador {computador} x {jogador} Você")
    if jogador == 2:
        print("===" * 15)
        print("Você venceu do computador!!! Parabéns.")
        print("===" * 15)
    elif computador == 2:
        print("===" * 15)
        print("O computador venceu!!! Tente novamente.")
        print("===" * 15)