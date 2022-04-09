
#-------------------------------------------------

#--------------  Algoritmo 123  --------------------

#-------------------------------------------------

#Ler três números, os possíveis lados de um triângulo, e imprimira classificação segundo os lados.
print("{:=^60}".format("Classificação de triângulos em relação aos lados"))
#receber 3 números:
n1=float(input("\nDigite o primeiro número: "))
n2=float(input("\nDigite o segundo número: "))
n3=float(input("\nDigite o terceiro número: "))

if n1<=(n2+n3) and n2<=(n1+n3) and n3<=(n2+n1):
    
    #classificar o tipo de triângulo de acordo com os lados
    #aquilátero = lados iguais
    if n1==n2 and n2==n3:
        print("Podem formar um triângulo equilátero.")

    #isóceles-> dois lados iguais
    elif n1 ==n2 or n1 == n3 or n2 == n3:
        print("Podem formar um triângulo isóceles.")

    #escaleno => lados diferentes
    else:
        print("Podem formar um triângulo escaleno.")
else:
    print("Os números não podem formar lados de triângulos")