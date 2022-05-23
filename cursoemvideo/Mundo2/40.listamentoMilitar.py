#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se 
# alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou 
# que passou do prazo.

from datetime import date

print("{:*^150}".format("\nAlistamento Militar\n"))
ano=int(input("Insira seu ano de nascimento : "))
sexo=input("Qual o seu sexo? F/M : ")
idade=date.today().year-ano
print(idade)

if sexo == "M":

    if idade == 18:
        print("Está a hora exata de se alistar!! ")
    elif idade < 18:
        print("Vc ainda vai se alistar daqui a {} anos em {}".format(18-idade, date.today().year +(18-idade) ))
    else:
        print("Já passou do tempo de alistamento amadoh..se liga hein! Era pra vc ter se alistado no ano de {}, {} anos atrás ".format(ano+18,idade-18))
elif sexo =='F':
    print("Você não precisa se alistar amadah! ")
else :
    print("sexo Invalido")