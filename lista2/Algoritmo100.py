#-------------------------------------------------

#--------------  Algoritmo 100  --------------------

#-------------------------------------------------

#Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o número formado pelos algarismos que estão nas casas das unidades de milhar e das centenas.

#ler um número inteiro de 4 dígitos
num=int(input("\nNúmero de 4 algarismos: "))

#guardar os algarismos que estão nas casas das unidades de milhar e das centenas
c=num//100

if c%4==0:
    print("\nO número é multiplo de 4: ",c)

else:
    print("\nO número não é multiplo de 4: ",c)