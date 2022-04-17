 
#-------------------------------------------------

#--------------  Algoritmo 185  --------------------

#-------------------------------------------------

print("Entrar com 15 números e imprimir a raiz quadrada de cada número.\n")

#entrar com 15 números
import math
for i in range(15):
    numero=int(input("Digite um número: "))
    
    #calcular e imprimir a raíz quadrada no número caso exista
    print(math.sqrt(numero)) if numero>=0 else print("Não faço raiz quadrada de número negativo!")