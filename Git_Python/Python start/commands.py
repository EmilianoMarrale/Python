message = "Hello world!"

equal_message = 'Hello world!!!!!!!!!!'

#Operazioni su stringhe

message.title() #Rende le iniziali delle parole maiuscole
message.upper() #Rende tutta la stringa maiuscola
message.lower() #Rende tutta la stringa minuscola
print("\t\n" + message) #\t fa il TAB \n fa il NEWLINE
message.rstrip() #Rimuove gli spazi a destra della stringa
message.lstrip() #Rimuove gli spazi a sinistra della stringa
message.strip() # Rimuove gli spazi a destra e a sinistra della stringa
# La concatenazione di stringhe si fa con il +

#Numeri

tot = (2 + 2) + (2 - 2) + (2 * 4) + (2 / 4) + (2 ** 2)
# I doppi asterischi fanno la potenza
print("integer tot num = " + str(tot)) # str converte un intero in stringa 

float_num = 1.0 + 4.0
print("float num = " + str(float_num))

 # Liste
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accesso agli elementi

print(bicycles[0] + " " + bicycles[3]) # Accesso al primo e quarto elemento
print(bicycles[-1] + " " + bicycles[-4]) # Accesso all'ultimo e al primo
# Il -1 restituisce sempre l'ultimo elemento della lista

# Modifica elementi
bicycles[0] = "ducati" ## Funziona anche con gli apici 'ducati'
print(bicycles[0])

# Aggiunta elementi (append)
bicycles.append('append_try')
print(bicycles[-1])

# Insert - Inserisce l'elemento all'indice specificato
bicycles.insert(0, "insert_try")
print(bicycles)

# Pop - Restituisce ed elimina l'ultimo elemento
popped_item = bicycles.pop()
print("Pop_try " + popped_item)
# Restituisce ed elimina l'elemento all'indice specificato
popped_specific_item = bicycles.pop(2)
print("Pop specific item: " + popped_specific_item)

# Delete
del bicycles[0] # Elimina il primo elemento (in posizione indice)
print(bicycles)

# Remove by value (Rimuove solo la prima occorrenza trovata)
bicycles.remove("ducati")
print(bicycles)

# Sort permanente (SORT)
bicycles.append("acqua")
bicycles.sort()
print(bicycles)

# Sort temporaneo (SORTED)
print(sorted(bicycles))

# Reverse di una lista
bicycles.reverse()
print(bicycles)

# Length di una lista
length = len(bicycles)
print("La lista è lunga " + str(length))

# Looping di lista
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician) # IL TAB è FONDAMENTALE ALTRIMENTI NON RICONOSCE IL BLOCCO
    