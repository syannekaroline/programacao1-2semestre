'''
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma 
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado 
(entre 0 e 20) e mostrá-lo por extenso.

'''

NumeroExtenso=("Zero","um","dois","Três","Quatro","Cinco","seis","Sete","oito","nove","Dez","Onze","Doze","Treze","quatorze","quinze","dezesseis","dezessete","Dezoito","Dezenove","Vinte")

while True:
    
    numero=int(input("Insira um número (0 até 20): "))

    while numero <0 or numero>20:
        numero=int(input("Insira um número no intervalo solicitado por favor !!: "))

    print("Número {} por extenso: {}".format(numero,NumeroExtenso[numero]))

    stop=input("Deseja continuar? [S/N]? ").strip().upper()[0]
    if stop=="N":
        break
    