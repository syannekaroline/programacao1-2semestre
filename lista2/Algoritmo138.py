
#-------------------------------------------------

#--------------  Algoritmo 138  --------------------

#-------------------------------------------------


#Ler um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.

#receber um número

numero=int(input("Insira um número pra corresponder a um mês: "))

#dicionário que contèm a chave e valores correspondentes ao meses
meses={"1":"janeiro","2":"Fevereiro","3":"Março","3":"Abril","5":"Maio","6":"Junho","7":"Julho","8":"Agosto","9":"Setembro","10":"Outubro","11":"Novembro","12":"Dezembro"}

#verificar se o número pertence ao intervalo 
if numero >= 1 and numero<=12:
    #varificar a qual mês o número se refere e imprimir
    print(f'O mês correspondente é : {meses.get(str(numero))}')
else:
    print("Não existe mês com esse número")