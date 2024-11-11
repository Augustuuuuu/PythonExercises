# Função que determina se o número é primo
def isprime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

numero = int(input("Digite um valor: "))

if isprime(numero):
    print(f"{numero} é um número primo")