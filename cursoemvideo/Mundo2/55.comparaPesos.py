'''Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final,
 mostre qual foi o maior e o menor peso lidos.

'''
menor=9999
maior=0
for i in range (5):
    peso=float(input("Insira o peso da {} pessoa: ".format(i+1)))
    if peso <menor:
        menor = peso
    if peso>maior:
        maior=peso

print("O maior peso foi o de : {}kg\nO menor peso foi de : {}kg".format(maior,menor))


