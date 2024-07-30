def isprime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

soma = 0
for i in range(3,500):
        if isprime(i):
            print(i)
