#-------------------------------------------------


#--------------  Algoritmo 97  --------------------

#-------------------------------------------------

print("\nEntrar com um número e informar se ele é divisível por 10, por 5, por 2 ou se não é divisível por nenhum desses")

#receber o número
numero=int(input("\nDigite um número: "))

#verificar se é divisível por 10 ou seja, se o resto da divisão por 10 é 0
if numero%10==0:
    print("\nMultiplo de 10!")
elif numero%5==0:#verificar se é divisível por 5
    print("\nMultiplo 5!")
elif numero%2==0:
    print("\nMultiplo de 2!")
else:
    print("\nNão é multiplo nem de 2 nem de 5")