'''
Listas - Aula 2 

listas dentro de listas

uma lista pode conter várias outras listas e da mesma forma tem como acessá-las por meio de índices

'''

lista=["syanne",19]
pessoas=[]
pessoas.append(lista[:])#criando um cópia da lista e adioconando em outra

print(lista)
lista.append(2002)
print(pessoas)

print(lista)

#dá pra ligar estruturas se ficar o append da lista sem [:] tudo o que acontecer em ujma acontece na outra
pessoas.append(lista)
lista.append(10)
print(lista)
print(pessoas)
lista.append("copia")
print(lista)
print(pessoas)


print("\nesvaziando as listas\n")

del lista[:]
del pessoas[:]
print(lista)
print(pessoas)

lista=[["syanne",1],["karoline",2],["moreira",3],["tavares",4]]

#formas de percorrer

for i in lista:
    print(i)

print("*"*10)

for i in lista:
    print(f"{i[0]} - {i[1]}º nome")

print("*"*10)  


for i , v in enumerate(lista):
    print(f" dado {i} - {v}")

print("{:*^60}".format("Recebendo valores"))

del lista[:]

for c in range (0,3):
    pessoas.append(input(f"insira um nome da {c+1}º pessoa: "))
    pessoas.append(int(input("insira a idade dela : ")))
    lista.append(pessoas[:])
    pessoas.clear()

print(pessoas)
print(lista)

print("*"*10)  
print("mostrando pessoas maiores e menores de idade: ")
maiores=menores=0
for i in lista:
    if i[1] >=18:
        print(f"{i[0]} é adulto - {i[1]} anos de idade")
        maiores+=1
    else:
        print(f"{i[0]} não é maior de idade - {i[1]} anos de idade")
        menores+=1

print(f"Numero de adultos : {maiores}")
print(f"Número de kids: {menores}")