#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro= float(input("Quanto vc tem na carteira? R$"))

#fazer a conversão pra dólar

dolar=dinheiro/4.72

print("Com R${:.2f} você pode comprar US${:.2f}".format(dinheiro,dolar))


