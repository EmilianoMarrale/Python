
# Esempio ZeroDivisionError

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Esempio FileNotFoundError
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

# Fail silently ESEMPIO. Nel caso in cui non voglio lanciare un eccezione e continuare come se nulla fosse successo (non informo l'utente)
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    pass                                         # Il pass consente il Fail Silently


# JSON Lettura e scrittura
import json

# Scrittura - JSON.DUMP
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# Lettura - JSON.LOAD
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
