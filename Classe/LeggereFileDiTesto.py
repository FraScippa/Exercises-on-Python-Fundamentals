
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
linee = fin.readline()
fin.close()

#3 modi: 1 voglio leggere il file (r), 2 lo voglio appendere ad un file(a), 3 lo voglio modificare(w).
#readlines legge tutte le righe incluso il carattere a capo (eol/eoln)
#Come faccio a togliere questi fine riga?
l1=[]

for l in linee:
    l1.append(l.strip()) #ritorna una copia della stringa senza gli spazi,tabulazione e fine riga
#solo ad inizio e fine riga.
linee=l1
print(linee)

s="alfa;beta;gamma"

#come posso ottenere la lista ["alfa,beta,gamma"]?
print(s.split(";")) #spezza la riga

