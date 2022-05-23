print('''
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.
''')

a1=int(input("Insira o primeiro termo: "))
r=int(input("Insira a razão: "))
ntermos=int(input("Vc deseja ver quantos termos dessa PA? "))

print("OS Primeiros {} termos dessa PA são: ".format(ntermos))
soma=0
an=a1+ntermos*r
for c in range (a1,an,r):

    print(c,"-> ",end="")
    soma+=c
print("A soma dos {} termos dessa PA é {}".format(ntermos,soma))

