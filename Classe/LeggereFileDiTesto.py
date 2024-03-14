
#Ho una stringa "123", la voglio trasformare in [1,2,3]
# definire una funzione che risolva il problema

def trasfStringa(sd):
    listaCifre=[]
    for _ in sd:
        listaCifre.append(int(_))
    return listaCifre

print(trasfStringa("123"))

#################################################################

fin = open("alice.txt", "r")
linee = fin.readline() #senza la s in "readlines" legge solo la prima riga.
fin.close() #do il comando di chiusura del file.

#3 modi: 1 voglio leggere il file (r), 2 lo voglio appendere ad un file(a), 3 lo voglio modificare(w).
#readlines legge tutte le righe incluso il carattere a capo (eol/eoln)
#Come faccio a togliere questi fine riga?
"""l1=[]

for l in linee:
    l1.append(l.strip()) #ritorna una copia della stringa senza gli spazi,tabulazione e fine riga
#solo ad inizio e fine riga.
linee=l1
print(linee)

s="alfa;beta;gamma"""

#come posso ottenere la lista ["alfa,beta,gamma"]?
#print(s.split(";")) #spezza la riga nel punto in cui ho messo il ";"

#Dato alice.txt, stampare, una per riga, tutte le parole che la compongono.

fin = open("alice.txt", "r")
linee = fin.readlines()

parole=[]

for l in linee:
    parole.extend(l.split(" "))


print(parole)   


#Data una lista di stringhe, eliminare dalla lista tutte le stringhe vuote.

ls=["uno","", "due", "tre","","","","","", "fine"]

listaFiltrata=[]

for i in ls:
    if len(i) > 0:
        listaFiltrata.append(i)

print(listaFiltrata)


def nonVuota(s):
    return s!=""

print(list(filter(nonVuota,ls))) #filter: vuole una funzione e come secondo parametro la lista da controllare.
       
#contare quanti caratteri ci sono in alice.txt
#contare quanti caratteri non sono spazi bianchi ci sono in alice.txt
#contare quanti caratteri alfanumerici [a-zA-Z0-9] ci sono in alice.txt

fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
print("caratteri: ", len(alice))

#####################################################

fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
notblank=0

for c in alice:
    if c!= " ":
        notblank +=1

print("caratteri not blank: ", notblank)

######################################################

fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
alfanum=0

for c in alice:
    if c in "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY":
        alfanum += 1

print("Caratteri Alfanumerici: ",alfanum)

#######################################################   

fin = open("alice.txt", "r")
alice = fin.read()
fin.close()
alfanum=0

for c in alice:
    if c != 0:
        alfanum+=1



    
    
    





