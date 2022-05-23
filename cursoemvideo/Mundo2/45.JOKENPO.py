#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from secrets import choice
from time import sleep

op=int(input('''Suas Opções: 
[0]Pedra
[1]Papel
[2]Tesoura
\nQual é a sua jogada? '''))

print("JO..")
sleep(1)
print("KEN..")
sleep(2)
print("PO!! ")


jogadas=("Pedra","Papel","Tesoura")

pc=choice(jogadas)

print("-="*60)
print("\nO computador escolheu {} \nJogador escolheu {}\n".format(pc,jogadas[op]))
print("-="*60)

if pc==jogadas[op]:
    print("EMPATE")
elif pc==jogadas[0] and "Tesoura"==jogadas[op] or pc==jogadas[1] and "Pedra"==jogadas[op] or pc==jogadas[2] and "Papel"==jogadas[op]:
    print("\033[1;33mO Computador Venceu!!\033[m")
else:
    print("\033[1;35mO Jogador Venceu!!\033[m")

