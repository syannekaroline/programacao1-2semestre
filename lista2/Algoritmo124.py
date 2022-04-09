#-------------------------------------------------

#--------------  Algoritmo 124  --------------------

#-------------------------------------------------

#Ler três números, os possíveis lados de um triângulo, e imprimira classificação segundo os ângulos.
print("{:=^60}".format("Classificação de triângulo em relação ao ângulo"))
#receber 3 números:
n1=float(input("\nDigite o primeiro número: "))
n2=float(input("\nDigite o segundo número: "))
n3=float(input("\nDigite o terceiro número: "))

if n1<n2+n3 and n2<n1+n3 and n3<n1+n2:
    if n1> n2 and n1>n3:
        maior=n1**2
        lados=n2**2+n3**2
    elif n2>n3:
        maior=n2**2
        lados=n1**2+n3**2
    else:
        maior=n3**2
        lados=n2**2+n1**2

    if maior==lados:
        print("\n Formam Triângulo Retângulo")
    elif maior>lados:
        print("Formam triângulo Obtusângulo")
    else:
        print("Formam triângulo Acutangulo")
else:
    print("As medidas não formam um triângulo")