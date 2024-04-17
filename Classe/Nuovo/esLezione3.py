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

d = {'pippo':2, 'pluto':1, 'topolino':5}
d1 = {}

#d1 = pippo 0.25 pluto 1/8 topolino 5/8 [stesse chiavi ma i valori= valore vecchio / tutti i valori] output

somma = sum(list(d.values()))

for key in d:
    d1[key] = d[key]/somma

print(d1)



    











