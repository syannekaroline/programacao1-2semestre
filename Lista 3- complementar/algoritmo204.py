#-------------------------------------------------

#--------------  Algoritmo 204  --------------------

#-------------------------------------------------
'''
Criar um algoritmo que leia um número da entrada (num), leia n números inteiros
da entrada e imprima o maior deles. Suponha que todos os números lidos serão
positivos. Exemplo:
'''

num=int(input("Quantos números desejas inserir? "))
maior=-999
for i in range(num):
    n=int(input("Insira um número: "))
    
    if n>maior : 
        maior=n
      
print("O maior entre os números inseridos é: ",maior)