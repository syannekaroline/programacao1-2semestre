#programa que imprime quantos anos faltam até sua aposentadoria

idade=int(input("Insira sua idade: "))
aposent=int(input("Com quantos anos vc vai se aposentar? "))

#usando o datetime <https://docs.python.org/pt-br/3/library/datetime.html> <https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python?gclid=CjwKCAjw9LSSBhBsEiwAKtf0n8N2bTSm1V6QU0KdAv4gsGCAZjj3Ba_x6t0d5Wt04xfbm6UJG_Mn6RoCLqwQAvD_BwE>
import datetime
x = datetime.datetime.now()
ano=(x.year)# ainda poderia ser ano=x.strftime('%Y') mas não executaria pois identificaria como string
faltam=aposent-idade#quantos anos faltam pra se aposentar
if faltam<0:
    
    print(f"Amado(a)! já era pra você ter se aposentado em {ano+faltam}, põe um cropped e reage, vc já pode se aposentar!")
else:
    print(f' Faltam {faltam} anos pra vc se aposentar. Estamos em {ano} e vc poderá se aposentar em {ano+faltam}')
