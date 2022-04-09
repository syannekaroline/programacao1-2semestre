#-------------------------------------------------

#--------------  Algoritmo 119  --------------------

#-------------------------------------------------

#Entrar com três números e imprimi-los em ordem decrescente (suponha números diferentes).

print("{:=^60}".format("Comparação da ordem decrescente entre 3 números"))

#receber 3 números:
n1=float(input("\nDigite o primeiro número: "))
n2=float(input("\nDigite o segundo número: "))
n3=float(input("\nDigite o terceiro número: "))

#verificar a ordem decrescente entre os números

# if n1<n2 and n2<n3:
#     primeiro=n3
#     segundo=n2
#     terceiro=n1
# elif n1<n3 and n3<n2:
#     primeiro=n2
#     segundo=n3
#     terceiro=n1
# elif n2<n1 and n1<n3:
#     primeiro=n3
#     segundo=n1
#     terceiro=n2
# elif n2<n3 and n3<n1:
#     primeiro=n1
#     segundo=n3
#     terceiro=n2
# elif n3<n1 and n1<n2:
#     primeiro=n2
#     segundo=n1
#     teceiro=n3
# elif n3<n2 and n2<n1:
#     primeiro=n1
#     segundo=n2
#     terceiro=n3

# print(f"Ordem decrescente: {primeiro} > {segundo} > {terceiro}" )

#comparando de forma mais eficiente

if n1>n2:#compara o primeiro com o segundo número
    aux=n1
    n1=n2#guarda o maior número em uma variável auxiliar e o menor no n1
    n2=aux # n2 recebe o maior número entre n1 e n2
if n1>n3: #compara o menor número com o n3 guarda o maior em uma variável auxiliar e o menor no n1
    aux=n1
    n1=n3
    n3=aux # n3 guarda o maior valor entre o menor valor e n3
if n2>n3: #compara os maiores valores em relação ao menor e compara os dois
    aux=n2
    n2=n3 #guarda o maior número em uma variável auxiliar e o segundo menor no n2
    n3=aux #guarda o maior no n3

print(f"Ordem decrescente: {n3} > {n2} > {n1}")