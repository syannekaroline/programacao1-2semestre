#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

'''
 Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

print("{:*^60}".format("\nResultado de Aprovação\n"))

n1,n2=map(float,input("Insira duas notas separadas por espaço: ").strip().split( ))

print("RESULTADO : ")

media=(n1+n2)/2
if media >=7:
    print("\033[1;35mAprovado com média {}\033[m".format(media))
elif media >=5 and media <7 :
    print("\033[1;32mRecuperação com média de {}\033[m".format(media))
else:
    print("\033[1;33mReprovado com média de {}\033[m".format(media))