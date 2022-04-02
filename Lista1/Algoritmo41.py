#--------------  Algoritmo 41  --------------------

#-------------------------------------------------
print("{:=^60}".format("Algoritmo 41"))

print("\nEntrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.\n")

a=float(input("Entre com 1 número: "))
b=float(input("Entre com 2 número: "))
c=float(input("Entre com 3 número: "))
d=float(input("Entre com 4 número: "))

mp=(a*1+b*2+c*3+d*4)/10

print("Média ponderada: ",mp,"\n")