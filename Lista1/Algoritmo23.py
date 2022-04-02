#-----------------------------------------------------------

#--------------  Algoritmo 23  ------------------------------

#-------------------------------------------------------------

#título que informa o número do algoritmo
print("{:=^60}".format("Algoritmo 23"))

#Comando pro usuário
print("Entrar comum número inteiro de 3 casas e imprimir o algarismo da casadas dezenas.")

a=int(input("Digite um número de 3 casas: "))

#retorno da questão pro usuário
d=a%100//10 # número de 3 algarismos é dividido por 100 e por isso o resto da divisão sempre será as casas da dezena e da unidade, depois é feita uma divisão inteira entre o resto e o 10, considerando assim apenas a casa da dezena

print(f"Algarismo na casa das dezenas:{d} \n")