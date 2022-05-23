'''
Exercício Python 62: Melhore o DESAFIO 61, 
perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

a1=int(input("Insira o primeiro termo: "))
r=int(input("Insira a razão: "))
ntermos=int(input("Vc deseja ver quantos termos dessa PA? "))

print("OS Primeiros {} termos dessa PA são: ".format(ntermos))

soma=0
an=a1+ntermos*r
termo=a1
n=ntermos

def PA(termo,r,an):

    while termo != an:
        print(termo,"-> ",end="")
        # soma+=termo
        termo+=r
    print("Pausa")
    # print("A soma dos {} termos dessa PA é {}".format(ntermos,soma))

PA(termo,r,an)

while ntermos !=0:
    aux=n
    ntermos=int(input("Quantos termos a mais deseja mostrar? "))
    n=ntermos+aux
    if ntermos ==0:
        break
    termo=an
    an=a1+n*r
    PA(termo,r,an)

print("Progressão finalizada com {} termos somados ".format(n))