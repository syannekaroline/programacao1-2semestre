'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, 
mostre uma listagem de preços, organizando os dados em forma tabular.
'''

dados=(

    input("Insira o nome do 1 produto: "),
    float(input("Insira o preço do 1 produto: ")),
    input("Insira o nome do 2 produto: "),
    float(input("Insira o preço do 2 produto: ")),
    input("Insira o nome do 3 produto: "),
    float(input("Insira o preço do 3  produto: ")),
    input("Insira o nome do 4  produto: "),
    float(input("Insira o preço 4 do produto: ")),
    input("Insira o nome do 5 produto: "),
    float(input("Insira o preço do 5 produto: "))
)

'''
nomes= dados[0:10:2]
precos=dados[1:10:2]

print("  Listagem de preços  ")
print("|{:^10}|{:^10} |".format("produtos","Valores"))
for i in range(5):
    print("|{:^10}| {:^10}|".format(nomes[i],precos[i]))
    print("-"*25)
'''

print("{:*^60}".format("\nLISTAGEM DE PREÇOS\n"))

for posi in range(0,len(dados)):
    if posi%2==0:
        print(f"{dados[posi]:.<30}",end="")
    else:
        print(f"R${dados[posi]}")