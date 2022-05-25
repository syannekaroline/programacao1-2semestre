
def isZero(entrada):
    num = float(entrada)
    return num == 0

def isNumeric(entrada):
    try:
        num = float(entrada)
        return True
    except:
        return False


entrada = input("Qual a taxa de retorno: ")
while((not isNumeric(entrada)) or isZero(entrada)):
    print("Desculpe, essa não é uma entrada válida.")
    entrada = input("Qual a taxa de retorno: ")

r = float(entrada)
print("Vai demorar {} anos para dobrar o investimento inicial.".format(72/r))