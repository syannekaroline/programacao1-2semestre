#--------------  Algoritmo 44  --------------------

#-------------------------------------------------
import math

print("{:=^60}".format("Algoritmo 44"))

print("\nEntrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo.\n")

num=float(input("Entre com o logaritmo: "))
base=float(input("Entre com a base: "))

logaritmo=math.log(num)/math.log(base)

print("\nO logaritmo de ",num,"na base",base,"é : ",logaritmo,"\n")