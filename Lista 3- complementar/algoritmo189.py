#-------------------------------------------------

#--------------  Algoritmo 189  --------------------

#-------------------------------------------------
#Criar um algoritmo que imprima a tabela de conversão de graus Celsius-Fahrenheit para o intervalo desejado pelo usuário. O algoritmo deve solicitar ao usuário o limite superior, o limite inferior do intervalo e o decremento. Fórmula de conversão: C =5 (F - 32) / 9

#solicitar o limite superior
lsup=int(input("Insira o limite superior de temperatura em Fahrenheit: "))

#solicitar o limite inferior
linf=int(input("Insira o limite inferior de temperatura em Fahrenheit: "))

#solicitar o decremento
dec=int(input("Insira o decremento em Fahrenheit:"))

for t in range(lsup,linf,-dec):
   
   C=5*(t-32)/9

   print("Temperatura em Farenheit: {} - Temperatura em celsius: {:.2f}".format(t,C))