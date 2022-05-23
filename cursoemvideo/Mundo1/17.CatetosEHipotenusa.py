import math

'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''
co=int(input("Insira o valor do cateto oposto "))
ca=int(input("Insira o valor do cateto adjacente: "))

H=math.sqrt(ca**2+co**2)#ou poderia elevar a 1/2 que é a msm coisa que raiz quadrada
H=math.hypot(ca,co)
print("A hipotenusa de um triângulo retângulo com cateto oposto igual a {} e cateto adjacente igual a {} vale {}.".format(co,ca,H))