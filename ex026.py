frase = str(input('Digite um frase qualquer: ')).upper().strip()
qa = frase.count('A')
pa = frase.find('A') + 1
pu = frase.rfind('A') + 1
print(f'A sua frase tem {qa} "a".')
print(f'O primeiro "a" encontrado na sua frase fica na posição: {pa}')
print(f'O último "a" encontrado na sua frase fica na posição: {pu}')
