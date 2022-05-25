
import re

stopwords = open("./base/stopwords2.txt", encoding='utf-8').read().split("\n")
texto5 = open("./base/texto5.txt", encoding='utf-8').read()


def clearText(text):
    '''Remove todos os caracteres especiais deixando somente as palavras separadas por 1 espaço. 
       O - e o \' contam com parte da palavra'''
    text = re.sub("[^\w\s\-']", " ", text).lower()
    #text = re.sub("\n", " ", text)
    return re.sub("\s+", " ", text).strip()

def filterStopWords(arr):
    newarr = []
    for w in arr:
        if w not in stopwords:
            newarr.append(w)
    return newarr

texto5 = filterStopWords(clearText(texto5).split(" "))

hist = {}
for p in texto5:
    if p in hist:
        hist[p]+=1
    else:
        hist[p]=1



histlist = list(hist.items())
histlist.sort(key=lambda i: i[1], reverse=True)

X,Y = zip(*(histlist[:10]))

# X = []
# Y = []
# for i in range(0,10):
#     X.append(histlist[i][0])
#     X.append(histlist[i][0])

print(X)
print(Y)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(X, Y, width=1, edgecolor="white", linewidth=0.7)
plt.xticks(rotation=45)
plt.show()