print("Hello world!!")

nome=input("Insira seu nome: ")

print(f'Olá {nome}, tudo bem? Seja bem-vindo(a)')

#alinhamentos

print(f"{'texto alinhado à direita' : >20}")
print(f"{'texto alinhado à esquerda' : <30}")
print(f"{'Texto centralizado':^60}")

texto='tô com sono'

#alinha à direita com espaços em branco
print("{0:>20}".format(texto))

#alinha a direita com smbolos #

print("{0:#>20}".format(texto))

#alinha de maneira central entre sìmbolos #

print("{0:#^60}".format(texto))
