from math import sqrt
from math import asin
from math import sin
from math import cos
from math import radians

#Calcolare la distanza tra Oslo (59.9°N 10.8°E) e Vancouver (49.3°N -123.1°W)
#d= 2r arcsin (sqrt) sin**2 1/2 (ϕ2-ϕ1)+ cos ϕ1 cosϕ2 sin2 1/2 (λ2-λ1)
#raggio della terra= 6371

#ϕ1= radians(float (input("inserisci latitudine 1: ")))
#λ1= radians(float (input("inserisci longitudine 1: ")))

#ϕ2= radians(float (input("inserisci latitudine 2: " )))
#λ2= radians(float (input("inserisci longitudine 2: ")))

#r=6371 #km

#z=2*r*asin(sqrt(sin(1/2*(ϕ2-ϕ1))**2+cos(ϕ1)*cos(ϕ2)*sin(1/2*(λ2-λ1))**2))

#print(f"La distanza è: {z}")


""" Definire

    due variabili (i1, i2) di tipo intero
    due variabili (s1, s2) di tipo stringa
    due variabili (f1, f2) di tipo float #un numero con la virgola
    due variabili (b1, b2) di tipo boolean

stampare
i1+i2
s1+s2
f1+f2
b1+b2
i1+s1
s1+i2
i1+f2
f2+i2
i1+b1
f1+b1
s1+b1
b1+i1
b1+s1
b1+f1"""

i1=10
i2=20
s1="34"
s2="45"
f1= 5.5
f2= 6.7
b1= True #1
b2= False #0


print(i1+i2)
print(s1+s2)
print(f1+f2)
print(b1+b2)
#print(i1+s1)
#print(s1+i2)
print(i1+f2)
print(f2+i2)
print(i1+b1)
print(f1+b1) #somma con un boolean se questo è true sommo di 1 se e falso sommo 0
#print(s1+b1)
print(b1+i1)
#print(b1+s1)
print(b1+f1)







