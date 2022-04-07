#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#perguntar a quantidade de quilometros percorridos
km=float(input("Insira a quantidade de quilometros percorridos: "))
#perguntar a quantidade de dias pelos quais ele foi alugado
dias=int(input("Insira a quantidade de dias pelos quais o carro foi alugado: "))
#receber o preço do aluguel por dia + 0,15 por quilometro rodado
preço_dia=float(input("Insira qual o valor do aluguel do carro por dia: "))
#calcular o preço a pagar
total_pago=preço_dia*dias+15/100*km
#mostrar o resultado dos dados calculados pro usuário
print("O aluguel de um carro que rodou {}km por {}dias a um valor de {}por dias mais R$0,15 por km rodado erá custar R${:.2f}".format(km,dias,preço_dia,total_pago))