

quant = int(input("Quantos números deseja somar: "))

sum = 0
for x in range(quant):
    num = float(input("Entre com um número: "))
    sum += num

print("O total é {}".format(sum))
