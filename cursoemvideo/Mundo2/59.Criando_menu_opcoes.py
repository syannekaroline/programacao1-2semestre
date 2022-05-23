'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

'''
from time import sleep
v1,v2=map(float,input("Insira dois valores separados por espaço: ").strip().split( ))
print('''\033[1;35m----------Operações----------
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] Digitar novamente

[ 5 ] sair do programa\033[m''')

operacoes="+x"
opcao=0
while opcao != 5:

    print("\033[m-="*10)
    opcao=int(input("\nQual a opção desejada? "))
    if opcao==1:
        print("\033[1;33m{} {} {} = {}".format(v1,operacoes[0],v2,v1+v2))
    elif opcao==2:
        print("\033[1;33m{} {} {} = {}".format(v1,operacoes[1],v2,v1*v2))
    elif opcao==3:
        print("\033[1;33m{} > {}".format(v1,v2) if v1>v2 else "{} >{}".format(v2,v1))
    elif opcao==4:
        v1,v2=map(float,input("Insira dois valores separados por espaço").strip().split( ))
    elif opcao==5:
       print("finalizando...")
       sleep(1)

    else: 
        opcao=int(input("\033[1;33mOpção inválida ! insira novamente: \033[m"))

print("Programa finalizado com sucesso!")
    

