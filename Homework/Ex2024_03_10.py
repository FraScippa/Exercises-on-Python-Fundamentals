#numero negativo o positivo
"""x = float(input("inserisci numero: "))

if x > 0:
    print(f"{x} è un numero positivo!")

elif x < 0:
    print(f"{x} è un numero negativo!")

else:
    print(f"{x} è 0")"""

#########################################################################################
    
#per vedere se un anno è bisestile, si puo dividere per 4, ma non per 100, a meno che non sia divisibile per 400.
"""y = int(input("inserisci anno: "))

if y % 4 == 0 : #AND entrambe devono essere vere. Usa sempre gli operatori logici per collegare le condizioni!!
    print(f"{y} è un anno bisestile.")

elif y % 100 != 0 and y % 400 == 0:
    print(f"{y} è un anno bisestile.")

else:
    print(f"{y} non è bisestile.")"""

##########################################################################################

#per vedere se un numero è pari o dispari
"""x = int(input("inserisci numero: "))

if x % 2 == 0:
    print(f"{x} è pari!")

else:
    print(f"{x} è dispari")"""

##########################################################################################

#Calcolatrice
"""operatori= {"+","-","*","/"}

x = input("inserusci primo numero: ")
z = input("operatore (possibili valori: +-*/)")
y = input("inserisci secondo numero: ")
risultato = 0

if x.isdigit() and y.isdigit() and z in operatori:  #x.isdigit: controlla che la scritta sia fatta di numeri, ma li lascia come stringa.
    
    u = float(x)
    i = float(y)
    
    if z == "+":
        risultato=u+i

    elif z == "*":
        risultato=u*i

    elif z == "/":
        risultato=u/i

    else:
        risultato=u-i
    print(f"il risultato è: {risultato}")        
else:
    print("errore nei dati inseriti. Controllare")"""

##########################################################################################










    








