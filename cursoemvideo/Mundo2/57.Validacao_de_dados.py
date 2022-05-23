'''
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter 
um valor correto.
'''

sexo=input("Insira seu sexo: [F/M]: ")

while sexo!="F" and sexo !="M":
    sexo=input("Valor Invalido! Insira novamente [F/M]: ")
print("Sexo: ","Feminino" if sexo=="F" else "Masculino")

print("\nOutra forma de fazer : \n")
sexo=input("Insira seu sexo: [F/M]: ").strip().upper()[0]#aqui a se a pessoa digitar Masculino ou masculino tbm serpa considerada ou M

print(sexo)

while sexo not in "FM":
    sexo=input("Valor Invalido! Insira novamente [F/M]: ").strup().upper()[0]
print("Sexo {} cadastrado com sucesso: ".format(sexo))




