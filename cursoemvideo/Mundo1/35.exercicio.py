#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.

print("{:*^150}".format("\nAnalisador de triângulo:\n"))

s1,s2,s3=map(int,input("Insira os 3 segmentos semaparos por um espaço: ").split( ))

print("Os segmentos inserido podem formar um triângulo" if s1+s2>s3 and s2+s3>s1 and s3+s1>s2 else "Os segmentos não podem formar um triângulo")