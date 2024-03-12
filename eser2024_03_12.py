
import random

#Scrivi un programma che utilizzi un ciclo for per stampare 
#i primi 10 numeri della sequenza di Fibonacci.
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55

#se a è pari b+c se a è dispari b - c.
#metodi per vedere se un numero è pari o dispari

a = 10
b = 20 
c = 30 

if a%2==0:
    print(b+c)
else:
    print(b-c)

def Arit(a,b,c):
    
    if a%2==0:
        print(b+c)
    else:
        print(b-c)

Arit (10,11,12) #Arit, ha 3 parametri formali. Quelli nelle parentesi sono parametri attuali.
Arit (11,2,3)
Arit (101,1000,2)
a,b,c=10,20,30
Arit (b,c,a)

#secondo modo

#if a & 1==0: <--questa è più veloce

#terzo modo

#if math.floor(a/2)*2 == a: 

#quarto modo

"""while a>0:
    a=a-2
if a == 0:""" #non efficente.


#Scrivere una funzione ColoreCasuale() che torna una stringa
#casuale "rosso", "giallo", "verde", "blu", "arancio", "ciano"...

def coloreCasuale():
    
    colori= ["rosso","giallo","verde","blu","arancio","ciano"] 
    return colori[random.randint(0,len(colori)-1)] 
    
print(coloreCasuale())
print(coloreCasuale())   
print(coloreCasuale())   
print(coloreCasuale())    

#Ricordate che digit è uno tra 0,1,2,3,4,5,6,7,8,9
#Problema: scrivere una funzione che costruisce una lista
#contenente tutte le possibili combinazioni di quattro
#4 digit. 10.000 combinazioni

def generaListaDigit():
    lista=[]
    for i in range(0,10000):
        s=str(i)
        while len(s)<4:
            s="0" + s
        lista.append(s)
    return lista
print(generaListaDigit())

#Modificare la GeneraListaDigit per generare una lista di liste del tipo
#[[0,0,0,0], [0,0,0,1], [0,0,0,2], ..., [9,9,9,8], [9,9,9,9]]


#Data una stringa numerica, convertirla in una lista di digit [9,8,1,2,3]

def stringDigitsToList(sd): #sd: parametro formale. Ciò che inserisci "da fuori" (quello che deve essere convertito)
    lista=[]
    for c in sd: 
        lista.append(int(c))
    return lista
print(stringDigitsToList("98123"))

        





    












