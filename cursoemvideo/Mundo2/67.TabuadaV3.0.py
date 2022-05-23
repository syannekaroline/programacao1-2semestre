'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado 
for negativo.
'''

print("{:#^60}".format("\n       Tabuada\n"))

while True:
    n=int(input("Insira um número pra exibir sua Tabuada (insira um numero negativo pra parar a execução): "))
    if n<0:
        break
    print("\033[1;33m******Tabuada do número {}*********\n".format(n))
    for i in range (11):
        print("{} x {} = {} ".format(n,i,n*i))
    print("*"*59,"\033[m")


