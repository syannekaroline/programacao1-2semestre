'''
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
a1=int(input("Insira o primeiro termo: "))
r=int(input("Insira a razão: "))
ntermos=int(input("Vc deseja ver quantos termos dessa PA? "))
print("OS Primeiros {} termos dessa PA são: ".format(ntermos))
soma=0
an=a1+ntermos*r
termo=a1
while termo != an:
    print(termo,"-> ",end="")
    soma+=termo
    termo+=r
print("A soma dos {} termos dessa PA é {}".format(ntermos,soma))