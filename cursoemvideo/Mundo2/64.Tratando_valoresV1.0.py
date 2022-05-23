'''
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
numero=quantnumeros=soma=0
while numero!=999:
    soma+=numero
    quantnumeros+=1
    numero=int(input("Digite  um número [999 pra parar] : "))   
print("Vc digitou {} numeros e a soma deles é {}".format(quantnumeros-1,soma))