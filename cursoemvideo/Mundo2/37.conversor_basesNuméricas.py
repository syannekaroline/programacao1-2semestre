#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o 
# usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print("{:*^60}".format("\nConversão de bases numéricas\n"))
numero=int(input("Insira um número inteiro pra ser convertido: "))
base=int(input("Insira o código de Conversão de base: \n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\nCógido de Conversão: "))

if base == 1:
    print("Número {} em binário : {}".format(numero,bin(numero)[2:]))
    '''
    entes de eu saber que realmente o python tem conversor: 

    div=0
    while div != 1:
        div=numero//2
        i=numero%2
        numero=div
        print(i,end="")
    '''
elif base==2:
    print("Número {} em Octal : {}".format(numero,oct(numero)[2:]))


elif base==3:
    print("Número {} em Hexadecimal : {}".format(numero,hex(numero)[2:]))
else:
    print("Opção Inválida!")