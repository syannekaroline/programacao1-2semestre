#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numeros=list(map(int,input("Insira 3 valores separados por um espaço: ").split( )))
maior=0
menor=99999999
for i in numeros:
    if i>maior:
        maior=i
    if i < menor:
        menor=i
print("O maior número é {}\nO menor número é {}".format(maior,menor))