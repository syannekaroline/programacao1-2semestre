'''
Crie um programa que calcule a área de uma sala. Solicitar ao usuário
o comprimento e a largura da sala em pés. Em seguida, exiba a área
em pés quadrados e metros quadrados.
'''
print("{:=^60}".format("Área de uma sala"))

c=float(input("Qual o valor do comprimento da sala em pés?"))
l=float(input("Qual o valor da largura da sala em pés? "))

# m^2 = f^2*0,939

k=0.09290304 #em python n tem constante todo elemento é variável, pra ser constante é só não modificar, devem haver convenções ex: toda contante é definida por letra maiúscula

pesquadrados=l*c
metrosquadrados= pesquadrados*k

unidade=input("Qual unidade vc deseja usar?(M/P): ")

if(unidade=="M"):
    print("Área em metros quadrados: {:.3f}".format(metrosquadrados))

else:
    print("Área em pés quadrados: {:.3f}".format(pesquadrados))
  