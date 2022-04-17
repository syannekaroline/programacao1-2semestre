#-------------------------------------------------

#--------------  Algoritmo 210  --------------------

#-------------------------------------------------
'''
A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são

fornecidos pelo usuário; a partir dai., os termos são gerados com a soma ou sub-
tração dos dois termos anteriores, ou seja:

A1 = A11 + AI-2 para / ímpar
A1 = Ai- 1 - A1..2 para /par
Criar um algoritmo que imprima os 10 primeiros termos da série de FETUCCINE.
'''

#receber os dois primeiros termos

n1,n2=map(int,input("Insira os dois primeiros termos separados por espaço: ").split(" "))

#imprimir a sequência
print("Sequência de FECCINE: ")
print(f"\n{n1}  {n2}  ",end="")

for i in range(3,11):

    termo=n2-n1 if i%2==0 else n1+n2
    print(termo," ",end="")
    n1=n2
    n2=termo