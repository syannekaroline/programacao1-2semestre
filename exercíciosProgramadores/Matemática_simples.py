#crie um programa que receba 2 números e imprimir o resultado das 4 operações entre eles

n1=input("Insira o primeiro número: ")
n2=input("Insira o segundo número: ")
# restrições: Os valores provenientes de usuários serão strings. Certifique-se de converter esses valores em números antes de fazer as contas.

# Revise o programa para garantir que as entradas sejam inseridas como valores numéricos. Não permita que o usuário continue se o valor inserido não for numérico
if n1.isnumeric() and n2.isnumeric():
    n1=int(n1)
    n2=int(n2)
    print(f' {n1} + {n2} = {n1+n2} \n {n1} - {n2} = {n1-n2} \n {n1} * {n2} = {n1*n2} \n {n1} / {n2} = {n1/n2}')
else:
    print("Você precisa insirir valores numéricos!")
