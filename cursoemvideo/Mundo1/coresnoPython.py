'''
aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus 
programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades
'''

#sempre que quiser representar uma cor em python

#\033[(prencher com códigos até 3) m

#\033[style;texto;background m

'''
códigos pra estilo :
0 - none(sem estilo)
1 - bold(em negrito)
4 - underline(sublinhado)
7 - negative(inverte as cores da letra e do fundo)
'''

'''
cores do texto [30-37]     backgound 
                          mesma sequencia de cores mas do intervalo 40-47                         
30- branco
31 - roxo
32 - verde
33 - amarelo
34 -  azul
35 - roxo
36 - azul
37 - cinza

'''

#\033[m refaz as configurações padrões do terminal
#acabei de descobrir que nesse terminal do vs code é diferente
print("\033[30;1mOlá syanne\033[m")
print("\033[31;4mOlá syanne\033[m")
print("\033[32;7mOlá syanne\033[m")
print("\033[33;0mOlá syanne\033[m")
print("\033[34mOlá syanne\033[m")
print("\033[35;1;mOlá syanne\033[m")
print("\033[36mOlá syanne\033[m")
print("\033[37mOlá syanne\033[m")
