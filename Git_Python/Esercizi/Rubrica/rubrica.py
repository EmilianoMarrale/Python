from contatto import *
import json

class Rubrica():

    def __init__(self):
        self.contatti_json = "contatti.json"
        self.lista_contatti = {}

    def crea_contatto(self):
        nome = input("Inserisci nome: ")
        cognome = input("Inserisci cognome: ")
        posto_numero = ""
        numeri = []
        while posto_numero != 'Q':
            posto_numero = input("Inserisci etichetta numero e numero di telefono o Q per uscire: ")
            numeri.append(posto_numero)
            print(posto_numero)
        numeri.remove('Q')
        contatto = Contatto(nome,cognome, numeri)
        try:
            with open(self.contatti_json, 'a+'):
                lw = 0
            try:
                with open(self.contatti_json, 'r+') as file:
                    l = json.load(file)
                    self.lista_contatti = json.loads(l)
                    print(" LLLLLLLL " + self.lista_contatti)
            except:
                print("json load failed")

            with open(self.contatti_json, 'w') as file:
                self.lista_contatti[cognome] = contatto
                contatti_json = json.dumps(self.lista_contatti, default=vars, indent=True)
                json.dump(contatti_json, file)
        except FileNotFoundError:
            print("GG")
            
    def leggi_contatti(self):
        try:
            with open(self.contatti_json, 'r') as f:
                r = json.load(f)
                return r
        except FileNotFoundError:
            print("GG2")


            

