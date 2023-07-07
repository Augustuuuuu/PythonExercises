from random import shuffle
print('Desafio 020')
print('Hoje vamos sortear alunos para a apresentação do trabalho.')
print('Por favor, escreva o nome dos alunos.')
n = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n, n2, n3, n4]
shuffle(lista)
print(f'A ordem de alunos sorteada foi: {lista}')
