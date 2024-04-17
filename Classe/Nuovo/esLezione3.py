'''d = {'pippo':2, 'pluto':1, 'topolino':5}

keys = list(d.keys())

i = 0

somma = 0

while i < len(keys):
    key = keys[i]
    val = d[key]
    #sommare i valori
    somma = somma + val
    i += 1 
#stampa questa somma
print(somma)'''

##########################################################################

'''d = {'pippo':2, 'pluto':1, 'topolino':5}
d1 = {}

#d1 = pippo 0.25 pluto 1/8 topolino 5/8 [stesse chiavi ma i valori= valore vecchio / tutti i valori] output

somma = sum(list(d.values()))

for key in d:
    d1[key] = d[key]/somma #d1[key] tira fuori il valore

print(d1)'''

#crea diz con 2 chiavi: somma pari e somma dispari. Questo sarà la somma dei n pari della prima e la somma dei n dispari

l = [1,2,3,4,5,2,2,6,7,16]

d2 = {'somma_pari':0, 'somma_dispari':0}

for i in l:
    if i % 2 == 0 :
        d2['somma_pari'] += i 
    else:
        d2['somma_dispari'] += i

print(d2) 








    











