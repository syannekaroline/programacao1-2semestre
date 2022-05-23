'''
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e 
quantas mulheres têm menos de 20 anos.
'''
somaidades=0
idadeHVelho=0
novinhas=0
for i in range (5):
    print("********** {} pessoa **************".format(i+1))

    nome=input("Nome : ")

    idade=int(input("Idade: "))
    sexo=input("sexo [F/M]: ").upper()

    somaidades=somaidades+idade

    if sexo=='M' and idade>idadeHVelho:
        idadeHVelho=idade
        homemMaisVelho=nome

    if sexo=='F' and idade<20:
        novinhas+=1      
print("\nMédia da idade do grupo: {:.1f}\nNome do homem mais velho: {}\nNúmero de mulheres que tem menos de 20 anos: {}".format(somaidades/5,homemMaisVelho,novinhas))