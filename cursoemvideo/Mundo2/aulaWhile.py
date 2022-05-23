''''
laço de repetição while:
para quando não se sabe exataamente a quantidade/ limite condicionais

repetição limitada sim por uma condição mas não se sabe quantas vezes ao certo aquele loop será realizado

ex: dar 10 passos pra pegar uma maça - se sabe quantas vezes o loop será realizado
mas quando não se sabe quantos passos são pra chagar a maçã pode se fazer:

    ENQUANTO (não pegar a maçã):
        dê um passo
    *não se sabe a quantidade de vezes que esse loop será realizado mas se sabe a condição de realização
se trata de uma ESRTUTURA DE REPETIÇÃO COM TESTE LÓGICO(diferente de estrutura de repetição com variável de controle)


'''
print("imprimindo números com for:\n")
for c in range (11):
    print(c," ",end='')

print("\nusando o while: \n")

count=0

while count != 11:#quando a condição for alcançada ele não entra mais no laço ou seja, ele não vai imprimir o 11
    print(count," ",end="")
    count+=1
#sabendo o limite/a quantidade de repetições que serão realizadas pode-se usar o for ou o while agora quando não se sabe só dá pra usar o for

#ex: quer receber informações do usuário mas não se sabe quantas são
n=1
while n != 0:#flag - condição de parada
    n=int(input("\nInsira um inteiro positivo qualquer: [para parar de inserir digite 0]: "))

parada="S"

while parada != "N":#flag=ponto de parada
    sla=input("Insira alguma cadeia de caracter: ")
    parada=input("Deseja continuar Inserindo?[S/N] ").upper()

#pode-se utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código. É muito importante saber usar o break no Python, já que em alguns casos precisamos interromper um laço no meio do caminho.

#quando existe uma condição dentro do loop capaz de faze-lo parar
#usados em loops infinitos 

#while True (loop infinito)
soma=0
while True:

    n=int(input("Digite um número: "))
    if n==999:
        break
    soma+=n
print(f"Soma dos números: {soma}")