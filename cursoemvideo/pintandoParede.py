#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

#ler largura
largura=float(input("Insira o valor da largura em metros: "))
#ler altura
altura=float(input("Insira o valor da altura em metros: "))
#calcular a área
A=largura*altura
#calcular a quantidade de tinta necessária sabendo que 1 litro  pinta 2m quadrados
qtdtinta=A/2
print("Sua parede tem dimensão de {}x{} e sua área é de {:.2f} m^2".format(largura,altura,A))
print("Para pintar essa parede, você precisará de {:.2f} litros de tinta".format(qtdtinta))