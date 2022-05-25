import math

pessoas = int(input("Quantas pessoas vão comer? "))
fatias = int(input("Quantas fatias por pessoa? "))

pizzas = math.ceil(pessoas*fatias/8)
sobras = pessoas*fatias%8

print("Compre {} pizzas para que cada pessoa coma {} fatias.".format(pizzas, fatias))
print("Vão sobrar {} fatias".format(sobras))