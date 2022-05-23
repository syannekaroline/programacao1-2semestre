'''
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
 No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
soma=quant=0
while True:
    n=int(input("Digite um número inteiro(digite 999 se quiser parar): "))
    if n==999:
        break
    soma+=n
    quant+=1
print(f"Foram digitados {quant} números e a soma deles é : {soma}")

