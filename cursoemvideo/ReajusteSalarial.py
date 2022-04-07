#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario=float(input("Qual o salário do funcionário? "))
taxa=(float(input("Qual a porcentagem de aumento aplicada à esse salário? ")))/100
print("O salário que era de R${}, após um aumento de {}% será de R${:.2f}".format(salario,taxa,salario+salario*taxa))