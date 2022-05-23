'''
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
 só que agora utilizando um laço for.
'''

print("{:*^100}".format("Tabuada"))

numero=int(input("Vc deseja ver a tabuada de qual número? "))

for i in range (11):
    print("{} x {} = {} ".format(numero,i,numero*i))