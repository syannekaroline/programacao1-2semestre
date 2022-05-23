'''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:


'''

valor=float(input("Insira o valor a ser pago pelo produto? R$"))

opcao=input('''OPÇOES DE PAGAMENTO:
\n[1] à vista dinheiro/cheque 
\n[2] à vista no cartão
\n[3] em até 2x no cartão
\n[4] 3x ou mais no cartão
\n Opção desejada: ''')

if opcao=='1':
    print("Novo valor com desconto de 10% : R${:.2f}".format(valor-valor*0.1))
elif opcao=='2':
    print("Novo valor com 5% de desconto: R${:.2f}".format(valor-valor*0.05))
elif opcao=='3':
    print("Valor a ser pago é o valor formal de {:.2f}".format(valor))
else:
    print("Novo valor a ser pago com 20% de juros : R${:.2f}".format(valor+valor*0.2))