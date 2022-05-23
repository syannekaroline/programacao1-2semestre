from random import choice,shuffle
alunos=list(input("Insira o nome dos 4 alunos separados po um espaço: ").split( ))
ordem={"Primeiro","Segundo","Terceiro","Quarto"}
print("O aluno sorteado foi : {}".format(choice(alunos)))

#exercício 20 - 
shuffle(alunos)
print("Ordem de apresentação do trabalho: ")

for i in alunos :
    print("{}".format(i))