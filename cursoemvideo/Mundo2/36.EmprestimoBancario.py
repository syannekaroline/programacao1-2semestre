#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não 
# pode exceder 30% do salário ou então o empréstimo será negado.

print("{:*^150}".format("\nAprovar Empréstimo Bacário\n"))

valorcasa=float(input("Qua o valor da casa? R$"))
salario=float(input("Qual o salário do comprador? R$"))
anos=float(input("Em quantos anos pretede pagar ? "))

print("Para pagar uma casa de {} em {} anos o valor da prestação será de R${:.2f}".format(valorcasa,anos,valorcasa/(anos*12)))

if valorcasa/(anos*12)<= salario*0.30:
    print("\033[35;1mEmpréstimo Pode ser Concedido!! \033[m")
elif valorcasa/(anos*12) >salario*0.30:
    print("\033[33;1mEmpréstimo Negado!\033[m")