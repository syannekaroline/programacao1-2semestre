#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp=float(input("Insira um valor de temperatura em graus celsius: "))

#conversão pra fahrenhaeit
F=temp*9/5+32

print("A temperatuda de {}*C correnponde a {:.2f}*F!".format(temp,F))