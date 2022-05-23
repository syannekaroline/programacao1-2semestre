#fatiamento -

frase="Syanne Karoline Moreira Tavares" 

print(frase)
print(frase[7:15])#mostra a sting do indice 9 até o 14

print(frase[:15:2])#mostra a string do zero até o 14 puando de 2 em 2

#análise

print(f"Tamanho da frase: {len(frase)}")#retorna o tamanho da frase

print('quanta vezes "a" aparece na frase= {}'.format(frase.count('a')))#retorna quantas vezes o 'a' aparece na frase

print('quanta vezes "a" aparece na frase do indice 0 até o 7= {}'.format(frase.count('a',0,8)))#retorna quantas vezes o 'a' aparece na frase

print("função find localiza uma string e retorna o valor do indice de onde a string começou: {}".format(frase.find("Tavares")))
#frase.find() frase.rfind()-- apartir da direita

#transformação

#replace- reposiciona String

print("{}".format(frase.replace("karoline","karolinda")))

#.upper - põe a string em caixa alta

print(frase.upper())#é um método o que for maiúsculo ele mantém e o que tiver em minúsculo ele transforma

print(frase.lower())#transforma em minúscula

print(frase.capitalize())#a primeira letra fica maisuscula

print(frase.title())#analisa quantas palavras tem pelas posições do espaço e coloca a primeira letra de cada palavra sejam maiúscula

frase2="     sysy     sla   teste   "

print(frase2)
print(frase2.strip())#remove os espaços inúteis do início e do fim

print(frase2.rstrip())#remove os espaços inúteis da direita(right)
print(frase2.lstrip())#remove os espaços inúteis da esquerda(left)

#divisão
#split gera uma lista com todas as cadeias de caracteres
'''str.split(‘delimitador’)

Retorna uma lista com strings separadas por um delimitador. Como por exemplo, o comando: .'''

print(frase.split(" "))
print(frase2.split( ))

print(frase.split( )[0])
print(frase2.split( )[1])
'''
str.join(lista)

O oposto de str.split(). Intercala cada string da lista com a string str.

Como por exemplo, o comando:

‘—‘.join([‘aaa’, ccc, ttt]) retorna: “aaa—ccc—ttt”.'''

print('-'.join(frase.split( )))
print("".join(frase.split()))
