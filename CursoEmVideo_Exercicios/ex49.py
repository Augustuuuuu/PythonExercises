numero = float(input("Digite um número: "))

for produto in range(1,11):
    print(f"{numero:.0f} X {produto} = {numero*produto:.0f}")
