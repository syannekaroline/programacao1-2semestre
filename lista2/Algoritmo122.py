
#-------------------------------------------------

#--------------  Algoritmo 122  --------------------

#-------------------------------------------------
#Ler três números e imprimir se eles podem ou não ser lados de um triângulo.
print("{:=^60}".format("Verificação de formação de triângulo"))
#receber 3 números:
n1=float(input("\nDigite o primeiro número: "))
n2=float(input("\nDigite o segundo número: "))
n3=float(input("\nDigite o terceiro número: "))

#verificar se podem formar um triângulo se n1< n2+n3 um lado tem que ser menor que a soma dos outros dois 

if n1<(n2+n3) and n2<(n1+n3) :
    if n3<(n2+n1):
        print("Os números podem ser lados de triângulos")
else:
    print("Os números não podem formar lados de triângulos")