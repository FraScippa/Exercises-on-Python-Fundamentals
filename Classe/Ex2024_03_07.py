
import random 
import time 

start = time.time_ns()
lista = []

for v in range(1, 10000000):
    lista.append(random.randint(1, 1000000000))

end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

#Ricerca nella lista

start = time.time_ns()

trovati = 0

for v in range(1, 10):
    if random.randint(1, 1000000000) in lista:
        trovati += 1
end = time.time_ns()

print(
    f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}"
)

####################################################################################################

start = time.time_ns()
aSet = set()  #si fa in questo modo quando i valori vengono aggiunti dopo, se aggiunti subito basta un add.

for v in range(1, 10000000):
    aSet.add(random.randint(1, 1000000000))   

end = time.time_ns()

print(f"Il tempo richiesto è: {(end-start)/1000000000}")

#Ricerca nell'insiene. (è dinamica)

start = time.time_ns()    

trovati = 0

for v in range(1, 10):
    if random.randint(1, 1000000000) in aSet:
        trovati += 1
end = time.time_ns()

print(
    f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}"
)

#hash : mi fa "diventare" una stringa un numero. (è un programma) [viene usato nel SET]
#utilizzando il modulo, mi fa diventare il mio numero di una grandezza più piccola. (% n)


#Comprehesion

lista=[1,2,3,4,5]

lista2=[x*x for x in lista] #posso fare una nuova lista dove metto un'operazione e un ciclo for

print(lista2)

####invece che fare nel modo classico####

lista2 = []

for x in lista:
    lista.append(x*x)

#comando "zip" accosta 2 elementi 
    
lista_dispari = [x*2+1 for x in range-(0, 10)]
print(lista_dispari)

lista_numeri= [x for x in range(0,10)]

print(lista_numeri)

print(list(zip(lista_numeri, lista_dispari)))





