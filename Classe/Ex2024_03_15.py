
#Esempio 1
#Leggere da input una stringa, se minore di "lettera", stampare la stringa "minore", 
#se maggiore di "lettera" e minore di "tocco", stampare "intermedia", 
#se maggiore di "tocco" e minore di "what" stampare "maggiore", altrimenti stampare "massima"



#in una funzione puoi utilizzare il "pass" per evitare che ti dia 
#errore (se quella funzione non è stata ancora dichiarata)


#Leggere da un file (persone.txt) i nomi, cognomi e eta di un gruppo di persone. 
#organizzarli in un dizionario la cui chiave è il cognome e il cui valore è 
#una t-upla contenente i tre valori letti.

fin = open('persone.txt', 'r')
persone = fin.readlines()
fin.close()

"""lista1=[]
listina1=[]
listina2=[]

for x in persone:
    lista1.append(x.strip().split(','))
    
for y in lista1[0]:
    listina1.append(y.strip())
    
for z in lista1[1]:
    listina2.append(z.strip())


print("Nome: ",listina1[0],'Cognome: ',listina1[1], "età: ",listina1[2])
print("Nome: ",listina2[0],'Cognome:',listina2[1],'età:',listina2[2])"""



listaPersone = [x.strip().split(",") for x in persone] 
lista = [x.strip() for x in listaPersone[0]] 
lista1 = [x.strip() for x in listaPersone[1]]
lista2 = [x.strip() for x in listaPersone[2]] 
lista3 = [x.strip() for x in listaPersone[3]]


print(f"Nome: {lista[0]}, Cognome: {lista[1]}, Età: {lista[2]}")
print(f"Nome: {lista1[0]}, Cognome: {lista1[1]}, Età: {lista1[2]}") 
print(f"Nome: {lista2[0]}, Cognome: {lista2[1]}, Età: {lista2[2]}") 
print(f"Nome: {lista3[0]}, Cognome: {lista3[1]}, Età: {lista3[2]}")



























    



