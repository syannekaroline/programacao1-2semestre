'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

def naoaparece(valor,tupla):
    if valor not in tupla:
        return 1


tupla=(
    int(input("Insira o primeiro valor: ")),
    int(input("insira o segundo valor: ")),
    int(input("insira o terceiro valor: ")),
    int(input("insira o quarto valor: "))
)

valor=int(input(" Insira um valor pra saber quantas vezes ele apareceu:  "))
naoaparece(valor,tupla)


print("O número {} apareceu {} vezes".format(valor,tupla.count(valor)))

valor=int(input("Insira um valor pra saber a posição da sua primeira ocorrência: "))


print("esse número não foi inserido" if naoaparece(valor,tupla) else "O número {} apareceu pela primeira vez na posição {} ".format(valor,tupla.index(valor)+1))

print("numeros pares digitados: ")
for n in tupla:
    if n%2==0 :
        print( n, " ",end="")