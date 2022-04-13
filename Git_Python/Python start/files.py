# Apertura di un file e lettura del contenuto
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
# Il with chiude il file appena non serve più, si potrebbe usare il metodo close() ma il with è più sicuro

# La READ ritorna una stringa vuota appena raggiunge la fine del file, per eliminarla basta applicare rstrip()

# E' possibile fornire un file path per aprire un file di un'altra directory

# Leggere un file una linea per volta
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())  # rstrip per rimuovere lo spazio bianco aggiunto ad ogni lettura


# Creare una lista di linee a partire da un file

    lines = file_object.readlines()

# Scrittura in un file
filename = 'programming.txt'
with open(filename, 'w') as file_object:     # Modi di aprire un file: r, w, a (append), r+ (rd and wr). Se si omette il modo, python lo apre in read-only
    file_object.write("I love programming.")





