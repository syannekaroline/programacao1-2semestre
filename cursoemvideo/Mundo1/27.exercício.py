#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome=list((input("Insira se nome completo: ").strip()).split( ))
print("Pimeiro nome: {}\nUltimo nome: {}".format(nome[0],nome[len(nome)-1]))