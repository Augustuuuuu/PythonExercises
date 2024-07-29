import random
print('Desafio 019')
a = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
lista = [a, a2, a3, a4]
res = random.choice(lista)
print(f'O vencender foi {res}')
