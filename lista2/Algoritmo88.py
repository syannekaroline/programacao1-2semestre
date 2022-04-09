#-------------------------------------------------

#--------------  Algoritmo 88  --------------------

#-------------------------------------------------


print("{:*>30}{: ^30}{:*<30}".format("\n","*Calculadora*","\n"))
print("{: >20}{: >23}{: >26}{: >21}".format("+ Pra somar\n","- Pra subtrair\n","* Pra multiplicar\n","/ Pra dividir"))

resp=input("         Digite uma opção: ")

if resp=="+":
    a=float(input("\nDigite 1 numero com ponto: "))
    b=float(input("\nDigite 2 número com ponto: "))
    print("\nSoma: ",(a+b))
elif resp=="-":
    a=float(input("\nDigite 1 numero com ponto: "))
    b=float(input("\nDigite 2 número com ponto: "))
    print("\nSubtração: ",(a-b))
elif resp=="*":
    a=float(input("\nDigite 1 numero com ponto: "))
    b=float(input("\nDigite 2 número com ponto: "))
    print("\nMultiplicação: ",(a*b))
elif resp=="/":
    a=float(input("\nDigite 1 numero com ponto: "))
    b=float(input("\nDigite 2 número com ponto: "))
    print("\nDivisão: ",(a/b))
else:
    print("Opção não disponível!")