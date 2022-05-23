'''
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
'''


print("{:*^150}".format("\nAnalisador de triângulo:\n"))

s1,s2,s3=map(int,input("Insira os 3 segmentos semaparos por um espaço: ").split( ))

if s1+s2>s3 and s2+s3>s1 and s3+s1>s2 :
    print("Os segmentos inserido podem formar um triângulo\nClassificação do triângulo: ",end="" )
    if s1==s2==s3:
        print("EQUILÁTERO")
    elif s1!=s2!=s3 !=s1:
        print("ESCALENO")
    else:
        print("ISÓCELES")
    
else:
     print("Os segmentos não podem formar um triângulo")