import re

def isNotVazia(entrada):
    return len(entrada)>0

def isPeloMenos2(entrada):
    return len(entrada)>=2

def hasXLen(entrada, x):
    return len(entrada) == x

def isNumeric(entrada):
    return entrada.isnumeric()

def has2Letras(entrada):
    if re.search("^[A-Z][A-Z]$",entrada):
        return True
    else:
        return False

def isValidID(entrada):
    arr = entrada.split("-")
    if(len(arr)!=2):
        return False
    return has2Letras(arr[0]) and isNumeric(arr[1]) and hasXLen(arr[1],4)

def validar(dados):
    if(isNotVazia(dados["fname"]) and isNotVazia(dados["lname"]) and isPeloMenos2(dados["fname"]) and isPeloMenos2(dados["lname"]) and isNumeric(dados["zip"]) and isValidID(dados["ID"])):
        print("Não houve erros!")
        return True
    if(not isNotVazia(dados["fname"])):
        print("Primeiro nome não pode ser vazio")
    elif(not isPeloMenos2(dados["fname"])):
        print("Primeiro nome precisa ter pelo menos 2 caracteres")

    if(not isNotVazia(dados["lname"])):
        print("Segundo nome não pode ser vazio")
    elif(not isPeloMenos2(dados["lname"])):
        print("Segundo nome precisa ter pelo menos 2 caracteres")
    
    if(not isNumeric(dados["zip"])):
        print("O CEP deve ser somente numérico")

    if(not isNumeric(dados["ID"])):
        print("O ID deve ter esse formato: AA-1234")

    return False

dados_empregado = {}
dados_empregado["fname"] = input("Entre com o primeiro nome: ")
dados_empregado["lname"] = input("Entre com o segundo nome: ")
dados_empregado["zip"] = input("Entre com o CEP: ")
dados_empregado["ID"] = input("Entre com o ID: ")

validar(dados_empregado)

print(dados_empregado)