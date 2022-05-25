'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
lista=[]
while True:
    numero=int(input("Insira um valor pra lista: "))
    while numero in lista:
        numero=int(input("O número já foi inserido! Por favor insira outro valor: "))
    lista.append(numero)
    print("Valor Inserido com Sucesso! ")
    cont=input("Deseja inserir mais um valor[S/N]? ").strip().upper()
    if cont=="N":
        break

print(f"Valores Inseridos em ordem crescente: {sorted(lista)}")


