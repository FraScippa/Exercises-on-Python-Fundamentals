#Antonio, marco, andrea, luigi, tony, bruno, laura, anita, annarita, lucia, jhon, alice, mary
#i primi 2 vanno via ed entrano jhon, alice, mary
#altre due vanno sempre in ordine d'ingresso (primo entrato, primo uscire)
#stampare l'elenco delle persone presenti
#infine stampar le persone presenti in ordine alfabetico

stanza=[]

stanza.append("antonio")
stanza.append("marco")
stanza.append("andrea")
stanza.append("luigi")
stanza.append("tony")
stanza.append("bruno")
stanza.append("laura")
stanza.append("anita")
stanza.append("annarita")
stanza.append("lucia")
stanza.append("jhon")
stanza.append("alice")
stanza.append("mary")

stanza=stanza[2:]

stanza.append("jhon")
stanza.append("alice")
stanza.append("mary")

stanza=stanza[2:]

print(stanza)

stanza.sort()

print(stanza)


#Altra Soluzione

stanza=[
    "antonio",
    "marco",
    "andrea",
    "luigi",
    "tony",
    "bruno",
    "laura",
    "anita",
    "annarita",
    "luca",
]
stanza=stanza[2:]

stanza.extend(["jhon", "alice", "mary"])

stanza=stanza

print(stanza)

stanza.sort()
print(stanza)











