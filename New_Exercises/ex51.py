# Lendo os dados de entrada
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Iniciando a contagem dos termos
termo = primeiro_termo

# Imprimindo os 10 primeiros termos
print("Os 10 primeiros termos da PA são:")
for c in range(1, 11):
    print(f"{termo}", end=" -> ")
    termo += razao

print("FIM")
