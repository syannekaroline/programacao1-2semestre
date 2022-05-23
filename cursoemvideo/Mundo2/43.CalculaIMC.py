'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''
print("{:*^150}".format("\n\nCalculador de IMC\n\n"))
peso=float(input("Insira seu peso em KG: "))
altura=float(input("Insira sua Altura em metros: "))

imc=peso/altura**2
pesoideal=imc*altura**2
print("IMC: {:.1f}".format(imc))
print("Classificação de acordo com o índice de massa corporal: ",end="")
if imc < 18.5:
    print("Abaixo do peso!")
    print("Seu peso ideal é de {}kg vc precisa ganhar {}KG".format(pesoideal,pesoideal-peso))
elif imc <25:
    print("Peso ideal!")
elif imc<=30:
    print("Sobrepeso!")
elif imc <=40:
    print("Obesidade")
else:
    print("Obesidade Mórbida!!")


