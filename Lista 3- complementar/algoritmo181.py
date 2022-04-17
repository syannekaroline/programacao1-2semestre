def algoritmo181 ():

    #-------------------------------------------------

    #--------------  Algoritmo 181  --------------------

    #-------------------------------------------------

    #Criar um algoritmo que imprima todos os numeros de 1 ate 100 e a soma deles

    soma=0
    #imprimir os números de 1 até 100
    print("Números de 1 até 100: ")
    for i in range(1,100):
        print(f"{i},",end="")

        #realizar a soma dos núemros:
        soma+=i

    #imprimir a soma dos números
    print("\nSoma dos números de 1 até 100: ",soma)
