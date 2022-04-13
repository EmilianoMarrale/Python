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

print("Liste")
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
# Sort permanente invertendo lista
bicycles.sort(reverse=True)
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
    
# Range loop (prints from 1 to 4)
for number in range(1,5):
    print(number)

# Creare lista di numeri con range
numbers = list(range(1,6))
print(numbers)

#Crea lista da 2 a 10 con passo 2
even_numbers = list(range(2,11,2))
print(even_numbers)

# Min/Max/Sum di una lista di numeri
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("min: " + str(min(digits)))
print("max: " + str(max(digits)))
print("sum: " + str(sum(digits)))

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("CIaone ", players)
print(players[0:3])
# Looping Through a Slice
print("Here are the last three players on my team:")
for player in players[-3:]:
    print(player.title())

# Copiare una lista
# Per copiare una lista occorre usare lo slicing [:] senza indici
players_copy = players[:]
print(players_copy)
players_copy.pop()
print(players_copy)
print(players)

print("Tuples\n")
# Tuple
# Oggetti immutabili usati per contenere dati (Es dimensione immutabile di un rettangolo)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# Non è possibile modificare singolarmente i valori di dimensions accedendo ai singoli campi
# Ma è possibile aggiornare dimensions con nuovi valori es dimensions = (400, 60)

print("IF Statements\n")
# IF statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# N.B. && e || in python sono and e or

# Ricerca di elementi in una lista
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
elif user in banned_users:
    print(" You are banned")
else: 
    print(" fuck off")

# Booleans
true = True
false = False

if true is True: 
    print("True statement")
elif false is False:
    print("False statement")

# Dizionari 
print("Dizionario\n")

prodotti = {'prodotto': 'uva', 'prezzo': 50}
print("Prodotto: ", prodotti["prodotto"], "\nPrezzo: ", prodotti["prezzo"])

# Aggiunta chiave-valore
prodotti["nuova_chiave"] = " nuovo_valore"
print(prodotti) 

# Modifica valore
prodotti["prodotto"] = "grano"
print(prodotti)

# Elimina chiave-valore
del prodotti["nuova_chiave"]
print(prodotti)

# Looping su dizionario
for chiave, valore in prodotti.items():
    print("\n" + chiave)
    print(str(valore))

# Looping su chiavi
for chiave in prodotti.keys():
    print(chiave)

# Looping su valori
for valore in prodotti.values():
    print(valore)

# Nesting di dizionari
prodotti_1 = {"prodotto": "cola", "prezzo": 10}
prodotti_2 = {"prodotto": "pepsi", "prezzo": 9}
prodottoni = [prodotti, prodotti_1, prodotti_2]
print(prodottoni)
for prodotto in prodottoni:
    for p in prodotto.items():
        print(p)

# Dizionario con lista

pizze = {"carciospeck": ["carciofi", "speck", "grana"],
            "gambero": ["uovo", "gambero", "salsa"] }
for pizza, ingredienti in pizze.items():
    print(pizza)
    for ingrediente in ingredienti:
        print(ingrediente)
print(pizze)


# User inputs
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# age = int(input("What's your age "))
# print(str(age))

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to " + city.title() + "!")

# BREAK e CONTINUE sono validi 

# Funzioni con keyword arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

# Parametro opzionale (DEVE NECESSARIAMENTE ESSERE L'ULTIMO DELLA LISTA)
def opzionale(nome, cognome, secondo_nome=''):
    print(nome,secondo_nome,cognome)
opzionale("Emi", "scrofani", "maria")

# Numero di parametri opzionali
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Numero di parametri opzionali di keyword arguments(?)
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

# E' possibile definire le librerie creando un file .py contentente le funzioni definite ed implementate 
# e usare import nome_modulo per importare la "libreria"
# Si utilizzano le funzioni con nome_modulo.funzione(args) dove nome è la "libreria" e funzione è la funzione definita al suo interno

# E' anche possibile importare singole funzioni con from module_name import function_0, function_1, function_2

# Usando "as" è possibile rinominare la funzione importata from module_name import function_name as fn

# E' possibile importare tutte le funzioni con from module_name import * ed evitare di usare la DOT NOTATION nominata prima nel caso di 
# un import generico della libreria come import nome_modulo
