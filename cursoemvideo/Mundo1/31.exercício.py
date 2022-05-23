#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 
# parta viagens mais longas.

distancia=float(input("Qual a distancia da viagem em km? "))

print("\nO preço da passagem pe de R${:.2f} reais.".format(0.5*distancia) if distancia<=200 else "\nO preço da passagem é de R${:.2f} reais".format(0.45*distancia))
