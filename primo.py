from math import sqrt
from math import asin
from math import sin
from math import cos
from math import radians

#Calcolare la distanza tra Oslo (59.9°N 10.8°E) e Vancouver (49.3°N -123.1°W)
#d= 2r arcsin (sqrt) sin**2 1/2 (ϕ2-ϕ1)+ cos ϕ1 cosϕ2 sin2 1/2 (λ2-λ1)
#raggio della terra= 6371

ϕ1= radians(float (input("inserisci latitudine 1: ")))
λ1= radians(float (input("inserisci longitudine 1: ")))

ϕ2= radians(float (input("inserisci latitudine 2: " )))
λ2= radians(float (input("inserisci longitudine 2: ")))

r=6371 #km

z=2*r*asin(sqrt(sin(1/2*(ϕ2-ϕ1))**2+cos(ϕ1)*cos(ϕ2)*sin(1/2*(λ2-λ1))**2))




print(f"La distanza è: {z}")



