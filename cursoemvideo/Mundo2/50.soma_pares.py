print('''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
''')

numeros=list(map(int, input("Digite 6 números inteiros separados por um espaço: ").split()))
soma=0
print("Os números pares são : ",end="")
for i in numeros:
    if i%2==0:
        soma+=i
        print(i," ",end="")
print("\nA soma deles é {}".format(soma))
