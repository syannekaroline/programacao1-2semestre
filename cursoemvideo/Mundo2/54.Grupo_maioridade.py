'''
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

'''
from datetime import date
maiores=0
for i in range(7):
    ano=int(input("Digite o ano de nascimento da {} pessoa: ".format(i+1)))

    if date.today().year - ano >=18:
        maiores+=1
print("Quantidade de pessoas que atiginram a mior idade: {}\nQuantidade de pessoas que ainda não atingiram a maior idade: {}".format(maiores,7-maiores))