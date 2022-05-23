#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

print("{:*^150}".format("\nComparando números\n"))
n1,n2=map(int,input("Insira dois números Inteiros separados por espaço para compara-los: ").split( ))

if n1>n2:
    print(" O Primeiro valor {} é maior que o segundo {} ".format(n1,n2))
elif n1<n2:
    print("O segundo valor {} é maior que o primeiro {}".format(n2,n1))
else:
    print("Nâo existe valor meior ou menor, os dois são iguais")