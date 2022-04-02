#--------------  Algoritmo 42  --------------------

#-------------------------------------------------

print("{:=^60}".format("Algoritmo 42"))

print("\nEntrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante, co-secante e co-tangente deste ângulo.\n")

import math
angulo=int(input("Entre com um ângulo em graus: "))

rang=angulo*math.pi/180
print("Seno: {:.2}".format(math.sin(rang)))
print("Cosseno: {:.2f}".format(math.cos(rang)))
print("Tangente: {:.2f}".format(math.tan(rang)))
print("Cossecante: {:.2f}".format(1/math.sin(rang)))
print("Secante: {:.2f}".format(1/math.cos(rang)))
print("Cotangente: {:.2f}".format(1/math.tan(rang)))