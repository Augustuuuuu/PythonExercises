contador = 0
soma = 0
while contador < 6:
    numero = float(input(f"Digite o {contador + 1}º valor: "))
    contador += 1
    if numero % 2 == 0:
        soma += numero
print(f"A soma dos números pares informados é {soma:.2f}")