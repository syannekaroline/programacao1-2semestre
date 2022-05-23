"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
from math import floor

num= float(input("Insira um número decimal e te mostrarei a parte iteira dele : "))

print("A parte inteira do número {} é {}.".format(num,floor(num)))

#outras funções que fariam isso : trunc(num), int(num)(sem importar biblioteca nenhuma)