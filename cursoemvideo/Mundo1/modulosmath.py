import math

print("Raiz quadrada de um número: ")

num= float(input("Insira um número: "))

raiz = math.sqrt(num) # se tivesse sido apenas import math o comando deveria ser math.sqrt(num)

print('A raiz de {} é igual a {:.1f} '.format(num,raiz))


print(math.ceil(num))
print(math.floor(num))
