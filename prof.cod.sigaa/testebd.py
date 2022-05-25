

import sqlite3
con = sqlite3.connect('teste.db')


cur = con.cursor()

# Create table
# cur.execute('''CREATE TABLE empregados
#                (primeiroNome text, ultimoNome text, cargo text, dataSaida text)''')

# # # Insert a row of data
# cur.execute("INSERT INTO empregados VALUES ('John', 'Johnson', 'Manager', '2016-12-31')")
# cur.execute("INSERT INTO empregados VALUES ('Tou', 'Xiong', 'Software Engineer', '2016-10-05')")
# cur.execute("INSERT INTO empregados VALUES ('Michaela', 'Michaelson', 'District Manager', '2015-12-19')")
# cur.execute("INSERT INTO empregados VALUES ('Jake', 'Jacobson', 'Programmer', '')")
# cur.execute("INSERT INTO empregados VALUES ('Jacquelyn', 'Jackson', 'DBA', '')")
# cur.execute("INSERT INTO empregados VALUES ('Sally', 'Weber', 'Web Developer', '2015-12-18')")

# # Save (commit) the changes
# con.commit()

def addSpace(celula, num, lado="direito"):
    dif = num-len(celula)
    if(lado=="direito"):
        return celula+(dif*" ")
    else:
        return (dif*" ")+celula


def printTable(d):
    max = []
    for i in d[0]:
        max.append(len(i))
    for r in d:
        for a in r:
            if(len(a) > max[i]):
                max[i] = len(a)
    
    for r in d:
        for a in r:
            print(addSpace(a,max[i]), end=" | ")



data = []
for row in cur.execute('SELECT * FROM empregados ORDER BY ultimoNome'):
    data.append(row)


printTable(data)


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()