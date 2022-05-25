'''
listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuáis
portanto elas podem ser mutáveis por meio da manipulação dos índices ou métodos

MÉTODOS 

1- ADICIONAR ELEMENTOS NOVOS

1.1 No final da lista 
lista.append() | Adiciona um elemento no final da lista

1.2 - em uma posição específica

lista.insert(posição,item) insere na posição o item

2 - APAGAR ELEMENTOS

2.1 del lista[i] - remove o item de indice i da lista

2.2 lista.pop(i) - tem como passar como parãmetro o índice do elemento que se quer eliminar se não passar nenhum parâmetro ele elimina o último elemento

2.3 lista.remove(item) - tem como parâmetro o índice que se quer remover - remove pelo conteúdo

obs: se  for tentado remover um elemento ou um índice que não pertemcem à lista vai dar um erro
mas há como verificar se o item tá na lista pelo "for tananam in "


FORMA DE CRIAR UMA LISTA USANDO RANGE
 valores=list(range(4,11)) --> [4,5,6,7,8,9,10]

FORMA DIRETA
    valores=[1,2,3,2,5,4,7]

MÉTODO SORT
A função sort em Python ordena a lista no lugar, trocando os valores em seus índices. Quando chamamos a função ordenar em uma lista, uma nova lista não é retornada; em vez disso, a MESMA LISTA É CLASSIFICADA
diferente do sorted (lista) que cria/retorna uma nova lista

lista.sort()

PS = tando com o sorted(lista) quanto com o lista.sort() se pode classificar a lista de forma reversa 

lista.sort(reverse=True)
sorted(reverse=True)
'''
from random import randint
from turtle import clear
lista=[]# ou poderia ser lista = list()

lista=list(range(1,10))
print(lista)

lista=list(range(1,10,2))
print(lista)

lista.append(int(input("insira um valor pra ser adicionado na lista: ")))

print(lista)

lista.insert(int(input("insira a posição que deseja add um item; ")),int(input("insira o item pra ser add: ")))

print(lista,f" - Tamanho da lista: {len(lista)}")

print(f"Lista Ordenada com sorted: {sorted(lista)}")
lista.sort()
print(f"Lista Ordenada com sort() : {lista}")

print(f"Lista Ordenada de forma reversa sorted: {sorted(lista,reverse=True)}")
lista.sort(reverse=True)
print(f"Lista Ordenada reversa com sort(reverse=True) : {lista}")

letras=["a","b","c","d"]

print(sorted(letras,reverse=True))
lista.pop()
print("Lista removendo o último valor com pop() : {}".format(lista))

lista.pop(int(input("Qual o índice do elemento que vc deseja remover? ")))
print(lista)

lista.remove(int(input("Qual o item vc deseja remover? ")))#remove a primeira ocorrência desse item
print("\n",lista)

# recebendo diversos valores pra uma lista em uma mesma linha

lista=list(map(int,input("Insira vários valores pra lista separados por espaço: ").split( )))

print(lista)

#gerando lista com valores aleatórios
for i in range (0,len(lista)):

    lista.insert(i,randint(1,22))
    lista.append(randint(1,22))

print(lista)


print("removendo os 3 primeiros itens")
for i in range (0,4):

    lista.pop(i)# lista.pop(i) não remove os itens sequencialmente pois a cada loop os índices de modificam

print(lista)

print("\nteste remoção\n\n")
del lista[:3]#melhor pra remover itens sequencialmente

print(lista)
#printando de forma mais organizada

for i,v in enumerate(lista):
    print(f"Posição : {i} | valor : {v}")

for i in range(1,4):
    lista.append(int(input("Insira um valor: ")))

for i,v in enumerate(lista):
    print(f"Posição : {i} | valor : {v}")

#ao igualar listas cria uma ligação entre as listas ou seja, o que acontece em uma acontece com a outra tipo parabatais ou um boneco de vudu e a pessoa que ele representa KKK

lista2=lista
lista2.insert(1,22)
print(lista2)
print(lista)

del lista[:4]

print("forma de copiar sem criar ligação\n\n")
lista3=lista[:]
lista3.append(22)
print(lista)
print(lista2)
print(lista3)

