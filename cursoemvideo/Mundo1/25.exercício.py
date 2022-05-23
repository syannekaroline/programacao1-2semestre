#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome=(input("Insira seu nome completo: ").strip()).lower()
print(nome)
print("Seu nome tem silva? {}".format( 'silva' in nome))