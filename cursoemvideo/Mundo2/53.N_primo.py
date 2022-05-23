print('''

Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.''')
numero=int(input("Insira um número : "))
Ndiv=0
print("\nDivisores de {} : ".format(numero))
for i in range(1,numero+1):
    if numero%i==0:
        Ndiv+=1
        print(i," ",end="")

print("\n\033[1;35mO número {} é primo! \033[m".format(numero) if Ndiv==2 else " \nPortando o\033[1;33m número {} não é primo!\033[m".format(numero))