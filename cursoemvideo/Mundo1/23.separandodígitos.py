# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero=int(input("Insira um número de 0 até 9999: "))
n=str(numero)
print(f'Unidade: {numero%10}\nDezena: {numero//10%10}\nCentena:{numero//100%10} \nMilhar: {numero//1000%10}')

