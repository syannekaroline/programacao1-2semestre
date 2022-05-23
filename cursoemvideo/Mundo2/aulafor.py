'''
laço de repetição for :

repetição de blocos de comandos dependendo dos limites de condição

laço de variável de controle
'''

for c in range(5):
    print(c)
print("pega") 

for c in range(5,0,-1):
    print(c)
print("pega")

for c in range(5,-1,-1):
    print(c)
print("pega")

for c in range(0,10,+2):
    print(c)

print("ímpares")
for c in range(-1,10,+2):
    print(c)

inicio=int(input("Início: "))
fim=int(input("Fim: "))
passo=int(input("Passo: "))

for c in range(inicio,fim+1,passo):
    print(c)

frutas=list(input("Insira duas frutas favoritas separadas por espaço: ").split( ))

for f in frutas:
    print(f)

for f in frutas:
    print(f)
soma=0
for c in range(5):
    n=int(input("Digite um número: "))
    soma+=soma+n
print("Somatório = {}".format(soma))