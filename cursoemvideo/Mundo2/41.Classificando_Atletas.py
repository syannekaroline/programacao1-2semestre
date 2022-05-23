'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que 
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''
from datetime import date
print("{:*^60}".format("\nClassificando Atletas\n\n"))

anoNascimento=int(input("Insira o ano de nascimento do atleta para descobrir sua categoria: "))

idade=date.today().year-anoNascimento
print("O atleta tem {} anos".format(idade))
print("Categoria : ",end="")
if idade <=9:
    print("MIRIM")
elif idade<=14:
    print("INFANTIL")
elif idade<=19:
    print("JÚNIOR")
elif idade<=25:
    print("SÊNIOR")
else:
    print("MASTER")