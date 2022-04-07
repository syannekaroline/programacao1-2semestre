# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço=float(input("Qual o preço do produto? "))
desconto=(float(input("Qual o valor do desconto em porcentagem ? ")))/100
print("O produto que custava {} com um desconto de {}% agora custa R${:.2f} ".format(preço,desconto,preço-preço*desconto))