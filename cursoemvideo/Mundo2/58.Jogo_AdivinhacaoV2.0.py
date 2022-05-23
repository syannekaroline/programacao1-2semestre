'''
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número
 entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final 
 quantos palpites foram necessários para vencer.
'''
from random import randint
from time import sleep

print("{:*^150}".format("\nJOGO DA ADIVINHAÇÃO\n"))
nivel=int(input('''----Níveis ----:\n[1]- números de 0-10\n[2]- números de 0-100\n[3]- números de 0- 500\nQual o nível vc deseja jogar? '''))
print("\nVou pensar em um número..\n")

if nivel ==1:
    numero=randint(0,11)
elif nivel==2:
    numero=randint(0,101)
elif nivel==3:
    numero=randint(0,501)

sleep(2)

print("Pensei..Agora tente adivinhar: \n")
palpite=int(input("Qual foi o número que eu pensei? "))
Npalpites=1

while palpite != numero:
    print("Um pouco menor!" if palpite>numero else "Um pouco mais alto!")
    palpite=int(input("\033[1;33mErrou! tente adivinhar novamente\033[m.Qual foi o número que eu pensei? "))
    Npalpites+=1
    
print("\033[1;35mAEEE !! Você acertou na {} tentativa!!\033[m".format(Npalpites))