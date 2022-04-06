'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
'''
algo=input("Insira algo: ")

print('O que você acabou de inserir é um dado do tipo {}'.format(type(algo)))

#em python is.. . é um método embutido para a manipulação de strings 
print(f'é numérico? {(algo.isnumeric())}')#retorna True se todos os caracteres da string forem numéricos
print(f'é alfabético? {(algo.isalpha())}')#retorna True se todos os caracteres da string forem alfabéticos
print(f'está am caixa alta? {algo.isupper()}')
print(f'está em ninúsculo? {algo.islower()}')
print(f'Tem espaços? {algo.isspace()}')
print(f'Está capitalizado? {algo.istitle()}')#se a a string estiver em itálico por exemplo

