#--------------  Algoritmo 43  --------------------

#-------------------------------------------------
import math

print("{:=^60}".format("Algoritmo 43"))

print("\nEntrar com um número e imprimir o logaritmo desse número na base 10.\n")
num=float(input("Entre com um logarítimo: "))

logaritmo=math.log(num)/math.log(10)

print("\nLogarítmo: ",round(logaritmo,2),"\n")