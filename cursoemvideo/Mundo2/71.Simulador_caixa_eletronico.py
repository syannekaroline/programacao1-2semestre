'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print("{:*^100}".format("\nSimulador de Caixa Eletrônico\n"))

saque=int(input("Qual o valor a ser sacado?(valor inteiro) R$"))
#pegar o valor do saque e dividir por cada cédula pra ver a quantidade que cédulas que serão necessárias
count=0
cedula=50
while True:
    if saque >=cedula:
        saque-=cedula
        count+=1
    else :
        print("Total de {} cédulas de R${:.2f}".format(count,cedula))
        if cedula==50:
            cedula=20
        elif cedula==20:
            cedula=10
        elif cedula==10 :
            cedula=1
        if saque==0:
            break
# cinquenta=saque//50
# resto=saque%50
# vinte=resto//20
# resto=resto%20
# dez=resto//10
# resto=resto%10
# um=resto

# print(saque," ",cinquenta," ",vinte," ",dez," ",um,)


