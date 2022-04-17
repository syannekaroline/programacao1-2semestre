#-------------------------------------------------

#--------------  Algoritmo 202  --------------------

#-------------------------------------------------
"""
Criar um algoritmo que leia um número (num) da entrada e imprima os múltiplos
de 3 e 5 ao mesmo tempo no intervalo de 1 a num. Exemplo:
Numero lido: 50 Saída: 15 30 45
"""

#ler um npumero de entrada:

num=int(input("Insira um número amior do que 15:"))

if num>15:
    for i in range(1,num):
        if i%3==0 and i%5==0:
            print(i,",",end="")
else:
    print("Não existe!!")
