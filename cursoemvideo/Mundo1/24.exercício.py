#Verificando as primeiras letras de um texto

#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome=input("Insira o nome de uma cidade: ").strip()

print( nome[:5].upper() == "SANTO")

    