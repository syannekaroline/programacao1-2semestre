'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor 
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar 
valores.
'''

numero=quantnumeros=soma=maior=0
menor=999
parar="S"
while parar != "N":
    numero=int(input("Digite  um número: "))
    soma+=numero
    quantnumeros+=1
    if numero>maior:
        maior=numero
    if numero<menor:
        menor=numero
    parar=input("Deseja continuar [S/N]? ").upper().strip()[0]
print("Vc digitou {} numeros e a soma deles é {}\nMédia de todos os valores: {:.1f}\nMaior: {}\nMenor: {}".format(quantnumeros,soma,soma/quantnumeros,maior,menor))