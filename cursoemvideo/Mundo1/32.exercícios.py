#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano=int(input("Insira o valor de uma ano pra saber se ele é bissextoe digite 0 pra saber sobre ele: "))

if ano ==0:
    ano=date.today().year
print("O ano {} é bissexto ".format(ano) if (ano%4 and ano%100 or ano%400)==0 else "O ano {} não é bissexto! ".format(ano))

