#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#  80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada 
# Km acima do limite.
velocidade=float(input("Qual a velocidade atual do carro em km/h? "))

if velocidade>80 :
    
    print("VC foi MULTADO. Exedeu o limite de 80km/h e terá que pagar R${:.2f}".format((velocidade-80)*7))
print("Tenha um bom dia e dirija com segurança!!")