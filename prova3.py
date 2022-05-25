#questão 3 

#dicionário que guarda as informações sobre os livros 
#cada livro tem uma chave única

#nome, cpf, data do empréstimo, data da devolução, data da real devolução pra devolução 
dados =dict()

teste={"teste":" "}

#lista pros livros
livros=[]
#escolher a operação (cadastrar,emprestar,devolver,imprimir dados do livro)
operação=int(input(f" Insira o dígico correpondente à  operação que deseja realizar:  \n| 1 : Registro | 2 : Empréstimo | 3: Devolução | 4: imprimir dados dos livros | 5: sair |"))


#cadastrar 
if operação==1:
    dados["Nome"]=input("Insira o nome do livro: ")
    dados["CPF"]=int(input("Insira o seu CPF: "))
    dados["Data de Devolução"]=int(input("Insira a data de devolução: "))
    dados["Data da devolução"]=input("Insira a Data de devolução: ")
    dados["Data da real devolução"]=int(input("Insira a data da real devolução: "))
    
    livros.append(dados.copy())
if operação==2:
    if (input("Qual livro vc deseja emprestar? ") )
