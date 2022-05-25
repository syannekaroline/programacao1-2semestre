from getpass import getpass

users = {}
while(True):
    opcao = input("Escolha uma opção (entrar|registrar|fechar): ")

    if(opcao.lower() == "registrar"):
        user = input("Digite o nome do usuário: ")
        #Verifica se o usuário já existe
        if(user in users):
            print("Usuário já está cadastrado. Tente fazer login com a opção 'entrar'.")
            continue
        senha = getpass("Digite a senha do usuário: ")
        users[user] = senha
        print("Usuário {} cadastrado com sucesso!".format(user))

    elif(opcao.lower() == "entrar"):
        user = input("Digite o nome do usuário: ")
        if(user not in users):
            print("Usuário não está cadastrado. Tente se registrar com a opção 'registrar'.")
            continue
        senha = getpass("Digite a senha do usuário: ")
        if(users[user] == senha):
            print("Olá {}, seja bem vindo!".format(user))
        else:
            print("Você errou a senha, tente novamente...")

    elif(opcao.lower() == "fechar"):
        break