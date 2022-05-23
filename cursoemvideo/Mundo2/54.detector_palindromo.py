'''
exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase=("".join((input("Insira uma frase pra verificar se se trata de um palíndromo: ").upper().split( ))))

inv=len(frase)
for c in range(len(frase)):
    inv=inv-1
    if frase[c] != frase[inv]:
        print("\033[1;33mNão temos um palíndromo!\033[m")
        break
    
if inv ==0:
    print("\033[1;35mTemos um palíndromo!\033[m")