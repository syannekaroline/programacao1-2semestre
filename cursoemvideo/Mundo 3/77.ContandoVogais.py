'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras 
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, 
quais são as suas vogais.
'''

tupla=(
    input("Insira o primeira palavra ").lower(),
    input("insira o segundo palavra: ").lower(),
    input("insira o terceira palavra: ").lower(),
    input("insira o quarta palavra: ").lower()
)

vogais=("a","e","i","o","u")

for nome in tupla:
    print("palavra: {} ".format(nome))
    print(f"{'Vogal':^10}  | {'qnt vezes':^10}")
    for i in vogais: 
        if i in nome:
            print("|{:^10} | {:^10} | ".format(i,nome.count(i)))