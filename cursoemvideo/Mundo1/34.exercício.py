#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário 
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento 
# de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario=float(input("Qual o seu salário? "))

aumento=salario*0.15 if salario<=1250 else salario*0.1

print("O seu aumento é de R${:.2f} reais e seu novo salário é de R${:.2f}".format(aumento,aumento+salario))
