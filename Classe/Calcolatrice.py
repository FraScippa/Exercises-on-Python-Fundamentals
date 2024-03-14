#zip: mi torna indietro come collezione, per farlo tornare lista si mette "list".
# Stampa solo gli elementi che riese ad accoppiare. Ne accoppia solo 2.


numero = ""
virgola=False

while True:  #Va avanti fin quando non è True.
    c = input("Digita 0-9,+-/=: ")
    if len(c) > 0:
        c = c[0]
    if len(c)==0:
        continue
    # dovete leggere un numero sia intero, sia decimale
    # e stamparlo nella sua interezza quando viene
    # digitato un simbolo non numerico (+-/=)
    #
    # Terminerete quando varrà la
    if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]:
        # Stampate il numero letto
        print("Il numero è: ", numero)
        break
    elif c==",":   #elif: è if e else insieme.
        if not virgola:
            numero = numero + c 
            virgola= True
        else:
            continue
    else:
        # costruzione del numero
        numero = numero + c 






    

