#Crie um programa que solicite uma string de entrada e exiba uma saída que mostre a string de entrada e o número de caracteres que a string contém

string=input("Qual a string de Entrada? ")
# print("{} tem {} caracteres".format(string,len(string)))


if len(string)>0:
    print("{} tem {} caracteres".format(string,len(string)))
else:
    print("O usuário deve digitar algo no programa!!")





