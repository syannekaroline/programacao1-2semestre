#--------------  Algoritmo 40  --------------------

#-------------------------------------------------

print("{:=^60}".format("Algoritmo 40"))

print("Entrar com dois numeros inteiros e imprimir a seguinte \nSaída: \nDividendo: \nDivisor: \nQuociente: \nResto: \n")

val1=int(input("Entre com um valor: "))
val2=int(input("Entre com um dividendo: "))

quoc=val1//val2
rest=val1%val2
print(f"Dividendo: {val1}\nDivisor: {val2} \nQuociente: {quoc} \nResto: {rest}\n")
