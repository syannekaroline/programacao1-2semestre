#-------------------------------------------------

#--------------  Algoritmo 25  --------------------

#-------------------------------------------------

#título que informa o número do algoritmo
print("{:=^60}".format("Algoritmo 25"))

#Comando pro usuário
print("Entrar com uma data no formato ddmmaa e imprimir: dia, mês e ano separados.\n")

data=int(input("Informe data no formato ddmmtt: "))

dia=data//10000 
mes=data%10000//100
ano=data%100

print(f' Dia: {dia}\n Mês: {mes}\n Ano: {ano}\n')