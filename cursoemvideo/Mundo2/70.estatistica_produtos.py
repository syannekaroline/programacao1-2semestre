'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

print("{:#^103}".format("\nEstatísticas da Compra de Produtos\n"))
total=caros=count=barato=0
while True:
    nome=input("\nInsira o nome do produto: ")
    preco=float(input("Insira o preço do produto: R$"))
    count+=1
    total+=preco
    if preco>1000:
        caros+=1
    if preco<barato or count==1:
        barato=preco
        nomeBarato=nome
    continuar=input("Deseja Continuar [S/N]? ").strip().upper()[0]
    if continuar =="N":
        break

print("\n\033[1;33m********Dados Coletados*******\nTotal da compra dos {} produtos: {:.2f}\nQuantidade de produtos que custam mais de mil reais: {}\nNome do produto mais barato : {} - valor : R${:.2f}".format(count,total,caros,nomeBarato,barato))