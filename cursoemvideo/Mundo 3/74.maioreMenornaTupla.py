'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e
 também indique o menor e o maior valor que estão na tupla.

'''
from random import randint

#gerando números aleatórios pra tupla
tupla=(randint(1,100),randint(1,100),randint(1,100),randint(1,100),randint(1,100))

#imprimir a tupla gerada
print("A tupla gerada aleatóriamente é : ")
for i in tupla:
    print(i," ",end="")

#mostrar o maior e o menor gvalor

print("\nMenor valor: {}\nMaior Valor: {}".format(sorted(tupla)[0],sorted(tupla)[4]))
print("\nMenor valor: {}\nMaior Valor: {}".format(min(tupla),max(tupla)))

