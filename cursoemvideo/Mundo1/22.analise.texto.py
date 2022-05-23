'''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

'''

nome=input("Insira seu nome: ").strip()

print(nome.title())
print(f"Nome com letras maiúsculas: {nome.upper()}")
print(f"Nome com letras minúsculas: {nome.lower()}")
print("Quantas letras ao todo o nome tem sem considerar espaços= {}".format(len("".join(nome.split( )))))
print("Quantas letras tem o primeiro nome {}: {} letras".format(nome.split()[0],len(nome.split( )[0])))