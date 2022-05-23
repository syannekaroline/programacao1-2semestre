print(
'''
Exercício Python 48: Faça um programa que calcule a soma entre todos os números ímpares e que são múltiplos de três 
e que se encontram no intervalo de 1 até 500.
''')
soma=0
quant=0
for c in range(1,501,2):
    if c%3==0:
        quant+=1
        soma+=c
print( f"A soma total dos {quant} números solicitados é de {soma}" )