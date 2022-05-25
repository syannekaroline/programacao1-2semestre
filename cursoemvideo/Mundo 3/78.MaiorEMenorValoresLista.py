'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na 
 lista.
'''

lista=list(map(int,input("Insira valores Numéricos pra uma lista semaparados po um espaço: ").split()))

print(f"Maior valor inserido : {max(lista) } contido na(s) posição(ões): ",end="")
for i,valor in enumerate(lista):
    if valor==max(lista):
        print(i,", ",end="")

print(f"\nMenor valor inserido: {min(lista)} contido nas posições : ",end="")

for i , v in enumerate (lista):
    if v == min(lista):
        print(i,", ",end="")