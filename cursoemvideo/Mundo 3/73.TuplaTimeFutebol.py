'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

times=("Corinthians",
        "Palmeiras",
        "São Paulo",
        "Atlético Mineiro",
        "Botafogo",
        "Santos",
        "Fluminense",
        "Coritiba",
        "América"
        "Avaí",
        "Internacional",
        "Athletico",
        "Red Bull",
        "Flamengo",
        "Goiás",
        "Cuiabá",
        "Atlético",
        "Juventude",
        "Ceará",
        "Fortaleza",

)
print("*"*60)
print("\033[1;32m5 primeiros colocados do brasileirão em 24/05/2022: ")

for i in range(5):
    print("Colocação: {} | Time: {}".format(i+1,times[i]))

for time in times[:4]:
        print("| Time: {}".format(time))


print("*"*60)
print("\033[1;35mOs últimos 4 colocados: ")
for i in range(15,19):
    print("Colocação: {} | Time: {}".format(i+2,times[i]))

print("*"*60)
print("\033[1;36mTimes em ordem alfabética: ")

# sorted de strings as organizam em ordem alfabética
 
for time in sorted(times):

    print(f"{time}")


busca=input("\033[minsira o nome do time que vc deseja saber a posição: ").strip().title()

if busca in times:

    print("{} - posição : {} colocado".format(busca,times.index(busca)+1))
else:
    print("Esse time não tá no campeonado brasileiro de 2022")