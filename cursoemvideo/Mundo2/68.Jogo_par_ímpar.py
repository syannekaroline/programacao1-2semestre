'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
from time import sleep


print("{:*^60}".format("\nJogo ímpar ou par\n"))
count=0
while True:
        
    pc=randint(0,10)
    jogada=int(input("Insira sua jogada: "))
    op=input("Qual sua escolha, I(ímpar) ou P(par) ? ").strip()[0].upper()
    while op not in "PI":
        op=input("Qual sua escolha, I(ímpar) ou P(par) ? ").strip()[0].upper()
    print("LAgartii...")
    sleep(1)
    print("Já!!")

    if op=="I" and (jogada+pc)%2 ==0 or op=="P" and (jogada+pc)%2 !=0 :
   
        print("\033[1;33mJogador :{}\nPc: {}\nSoma: {} - {}\nJogador Perdeu!\033[m".format(jogada,pc,jogada+pc,"Par" if (jogada+pc)%2==0 else "ímpar"))
        break
    else:
        print("\033[1;35mJogador :{}\nPc: {}\nSoma: {} - {}\nJogador Venceu!\033[m".format(jogada,pc,jogada+pc,"Par" if (jogada+pc)%2==0 else "ímpar"))
        count+=1
print("Total de Vitórias Consecutivas: {}".format(count))