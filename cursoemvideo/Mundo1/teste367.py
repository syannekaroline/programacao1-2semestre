import random
conjunto1=[9]
conjunto2=[19]
elementos_diferentes=[]



  
for i in range(19):
  
  n2=random.randint(0,100)
  conjunto2.append(n2)

for i in range(9):
  n1=random.randint(0,100)
  conjunto1.append(n1)

  if n1 not in conjunto2:
    elementos_diferentes.append(n1)

for i in conjunto2:
  if i not in conjunto1 and i not in elementos_diferentes :
    elementos_diferentes.append(i)
# for i in range(19):
#   aux=0
#   for j in range(9):
     
#     if conjunto2[i] == conjunto1[j]:
#       aux+=1

#   if aux == 0:
#     elementos_diferentes.append(conjunto2[i])
    

print("Elementos do conjunto 1 :{} ".format(conjunto1))
print("Elementos do conjunto 2 :{} ".format(conjunto2))
print("Elementos não comuns : {}".format(elementos_diferentes))