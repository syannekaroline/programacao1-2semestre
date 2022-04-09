#-------------------------------------------------

#--------------  Algoritmo 108  --------------------

#-------------------------------------------------

#Entrar com o nome de uma pessoa e so imprimi-lo se o prenome for JOSE considerar: JOSÉ, José ou josé.

#receber o nome da pessoa
nome=str(input("Digite o nome: "))
#receber o prenome em uma variável
prenome=nome[:4]
#comparar o prenome com "JOSÉ","josé" ou josé

if prenome=="JOSÉ" or prenome=="José" or prenome=="josé":
    print("nome: ",nome)#imprimir caso a comparação seja verdadeira
