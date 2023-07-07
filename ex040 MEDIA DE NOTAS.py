print('\033[1;97mCALCULADOR DE MÉDIA')
nota = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota+nota2) / 2
print(f'Sua média foi: {media:.1f} pontos')
if media < 5:
    print('\033[1;31mREPROVADO')
elif 7 > media >= 5:
    print('\033[1;33mRECUPERAÇÃO')
elif media >= 7:
    print('\033[1;32mAPROVADO')
