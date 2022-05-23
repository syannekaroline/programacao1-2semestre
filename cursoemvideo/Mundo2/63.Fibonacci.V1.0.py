'''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
'''

print("===========Sequência de fibonacci===========")

N=int(input("Quantos elementos da sequência vc deseja ver? "))
t1=0
t2=1
count=2

print("{} primeiros termos da sequencia de fibonacci: ".format(N),end="")
aux=0

print(t1,' ->',t2,' -> ', end="")
while count != N:
    t3=t1+t2
    t1=t2
    t2=t3
    print(t3," -> ", end="")
    count+=1
print("FIM")