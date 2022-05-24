'''
Tuplas são variáveis compostas

toda variável simples é armazenada em um espaço da memóriaa

dá pra atribuir vários valores pra uma mesma variável
no python dá pra fazer isso de 3 formas : 
1- tuplas
2- listas 
3 - dicionários

tuplas são variáveis que armazenam vários valores e cada valor é acessado por índices podendo-se dessa forma usar fatiamento para acessa-las
ex: lista=(banana,maça,pera)
lista[1:]= maça, pera
lista[-1]=pera=lista[3]

funções importantes:

tamanho 
função len(lista) = retorna quantos elementos se tem na lista

estrutura de repetição

for i in lista
    print(lista)

DETALHEE = AS TUPLAS SÃO IMUTÁVEIS - NÃO HÁ COMO ALTERAR ELEMENTOS DE DENTRO DE UMA TUPLA APENAS ACESSÁ-LOS

'''

#CRIANDO tuplas - usa-se parênteses

lanche=("Hambúrguer","suco","pizza","pudim")#não necessáriamente preci usar parênteses mas é melhor usar

#manipulação de tuplas:]

#1- fatiamento
print(lanche)
print(lanche[1])
print(lanche[-4])
print(lanche[-1])
print(lanche[2:])
print(lanche[2:3])#desconsidera p último quando é assim
print(lanche[:2])
print(lanche[2:-1])

print("*"*60)

#tuplas são imutáveis
# lanche[0]="baton de chocolate" -- vai dar erro pois não se pode modificar elementos das tuplas pois são imutáveis

for comida in lanche:
    print(comida)

print("*"*60)

#outra forma de utilizar o for - interessante pra quando for mostrar o índice do contador
for i in range(0,len(lanche)):
    print(lanche[i],f"posição:  {i}")

#outra forma de fazer 
print("*"*60)

for pos, comida in enumerate(lanche):#além do dado ele dá a posição por isso tem duas variáveis primeira pra comida e depois pro valor
    print(f"Eu vou comer {comida} na posição {pos}")

#ordenar - sorted é um método que ordena uma tupla

print(sorted(lanche))#do maior pro menor - desse caso da maior string pra menor
print(lanche)

numeros1=(2,4,1,6,)

print(numeros1)
print(sorted(numeros1))

print("uniao de tuplas")

numeros2=(7,2,9,2)
print(numeros1)

print(numeros1+numeros2)
print(numeros2+numeros1)
print(len(numeros2+numeros1))

#métodos internos

#.count(agumacoisa) - retorna quantas vezes alguma coisa aparece na tupla

print((numeros1+numeros2).count(2))#retorna quantas vezes o 2 apareceu
print("Quantas vezes aparece 'pizza ' na tupla lanche : {}".format(lanche.count("pizza")))

#index.(algumacoisa) - retorna o índice de algumacoisa dentro da tupla(primeira ocorrência)
print("Posição de pizza na tupla: {}".format(lanche.index("pizza")))

c=numeros1+numeros2
print(c)

print("Quantas vezes aparece 2 na tupla lanche : {}".format(c.count(2)))
print("Posição de 2 na tupla c: {}".format(c.index(2)))#primeira ocorrencia

#deslocamento
print("Posição de 2 na tupla c: {}".format(c.index(2,1)))#qual o indice apartir da posição 1

#tuplas podem armazenar valores de tipos diferentes
#não de pode imutar mas se pode apagar uma tupla da memória usando del del(c)

#maior e menor valor dentro da tupla - max(tupla) min(tupla)
