
# Definire una classe
class Dog():

    """A simple attempt to model a dog."""

    def __init__(self, name, age):                           # Costruttore - self = this, deve essere sempre presente
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

# Istanziare un oggetto 
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Accesso agli attributi e modifica
print(my_dog.name)
my_dog.name = 'luciano'
print(my_dog.name)

# Ereditarietà

class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# Per eseguire l'override dei metodi basta riscrivere il nome del metodo uguale a quello del parent

# Importare una classe: se Car(): fosse in un file car.py per importarla scriveremo from car import Car
# Se avessimo più classi e importassimo tutto il file car dovremo usare la DOT NOTATION per accedere agli oggetti
# Ad esempio car contiene ElectricCar GasCar e Car per accedervi useremo my_ecar = car.ElectricCar(nome,marca,etc..)
# Altrimenti come per le funzioni è possibile importare solo gli oggetti che ci interessano evitando di utilizzare la DOT NOTATION
# ES: from car import * (importa tutti gli oggetti)





