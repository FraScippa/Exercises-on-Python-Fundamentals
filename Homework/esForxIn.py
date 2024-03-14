"""
lista_nomi = [
    "Giovanni",
    "Luca",
    "Inid",
    "Federico",
    "Flaminia",
    "Maria", 
    "Francesca", 
    "Jhonny",
    "Andrea",
    "Sofia"
]

for x in range(0, len(lista_nomi)):
    if(len(lista_nomi[x])<8):
        print(f"Nome: {lista_nomi[x]} sufficientemente corto")
    else:
        print(f"Nome {lista_nomi[x]} troppo lungo")

"""

"""
u = input("Che lettera cerchi? ")
i = 0
for x in lista_nomi:
    for y in x:
        if(y.lower()==u):
            i+=1
print(f"La lettera {u} Ã¨ apparsa {i} volta/e")


array=["Hello", "bye", "good", "nice", "awesome"]

for x in array:
    for y in x:
        print(y)"""


for x in range(1, 10):
    print("*" * x)



"""lista=[5, 12, 8, 3, 10, 9000]

ditto=0

for x in lista:
    if(x>ditto):
       ditto=x
print(ditto)

y = 7
for x in range(1, 11):
    print(y*x)

s="Python"

for x in range(len(s)-1,-1,-1):   #len: conta partendo da 1 gli elementi nell'array. -1 posizione finale non inclusiva. -1 step per direzionarlo nella parte opposta.
    print(s[x])


x= int(input("inserisci numero: "))

for y in range(1,x):
    x*=y  #moltiplichi x*y ed allo stesso tempo assegna ad x il valore dell'operazione stessa.
    
print(x)"""