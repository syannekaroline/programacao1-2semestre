#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

print("{:*^160}".format("\nVou pensar em um número de 0 a 5...Tente adivinhar\n"))
numero= randint(0,5)
print("Acertou miserarvi" if int(input("Em que número eu pensei? ")) == numero else "errouuu pensei no numero não pensei no numero {}".format(numero))

