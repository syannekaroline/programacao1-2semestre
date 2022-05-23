#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase=(input("Insira uma frase: ").strip()).lower()

letra=(input("Qual letra vc deseja saber a primeira e a última ocorrência? ").strip()).lower()
vezes=0
primeira=99
ultima=0

for i in range(len(frase)):

    if frase[i] ==letra :
        vezes+=1
        if i<primeira:
            primeira=i
        if i>ultima:
            ultima=i

    
print("a letra {} aparece {} vezes \nPrimeira vez aparece na posição {}\nÚltima vez aparece na posição {}".format(letra,vezes,primeira,ultima))

 

print("\n\n\na letra {} aparece {} vezes \nPrimeira vez aparece na posição {}\nÚltima vez aparece na posição {}".format(letra,frase.count(letra),frase.find(letra),frase.rfind(letra)))
