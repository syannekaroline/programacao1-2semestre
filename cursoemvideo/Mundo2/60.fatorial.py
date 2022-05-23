'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
'''

print("{:*^60}".format("\nFatorial\n"))

numero=int(input("Insira um número: "))
fatorial=1
count=numero
print(numero,"! = ",end="")
while count != 0:
    print("{} x ".format(count) if count != 1 else "{} = ".format(count),end="")
    fatorial=fatorial*count
    count-=1
    
print("{}".format(fatorial))
print("\nFatorial de {} é {}".format(numero,fatorial))