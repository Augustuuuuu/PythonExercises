# Definir se a palavra é um palindromo


palavra = input("Digite uma palavra: ").lower()
palavra = palavra.replace(" ", "")
palavra_invertida = palavra[::-1]
palavra_invertida = palavra_invertida.replace(" ", "")


if palavra_invertida == palavra:
    palavra = palavra.replace("", " ")
    palavra_invertida = palavra_invertida.replace("", " ")
    print("É um palíndromo!")
    print(palavra)
    print(palavra_invertida)
else:
    print("Não é")