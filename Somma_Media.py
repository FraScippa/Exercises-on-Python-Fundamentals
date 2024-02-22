
#calcola la somma 
import random

lista=[]

"""for x in range(1,1000001):
    lista.append(x)

SommaLista=sum(lista)

print(SommaLista)

#calcola la media

media=SommaLista/1000000

print(media)"""


#generatore randomico

for y in range(1000001):
    NumeroRandom=random.randint(1,1000001)
    lista.append(NumeroRandom)

SommaRandom=sum(lista)

print(SommaRandom)

#media 

media=SommaRandom/1000000

print(media)





