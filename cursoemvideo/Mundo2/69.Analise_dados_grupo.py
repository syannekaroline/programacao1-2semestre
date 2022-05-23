'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''
maiores=homens=novinhas=0
print("{:*^60}".format("Análise de dados de um Grupo de pessoas"))
while True:
    nome=input("Nome: ").strip()
    idade=int(input("Idade: "))
    sexo=input("Sexo [F/M]: ").strip().upper()[0]
    print("{} foi cadastrad{} com sucesso! ".format(nome,"a" if sexo=="F" else "o"))

    if idade>=18:
        maiores+=1
    if sexo=="M":
        homens+=1
    if sexo=="F" and idade<20:
        novinhas+=1

    parar=input("Deseja continuar [S/N]? ").strip().upper()[0]
    if parar =="N":
        break
print("\n\n*******Dados recolhidos : ********\nQuantidade de pessoas com mais de 18 anos: {}\nNúmero de homens que foram cadastrados: {}\nQuantidade de mulheres que tem menos de 20 anos: {}".format(maiores,homens,novinhas))