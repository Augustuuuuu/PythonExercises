# Função que verifica se o número é primo
soma = 0
for i in range(3,500):
        if i % 3 == 0:
            soma += i
print(soma)