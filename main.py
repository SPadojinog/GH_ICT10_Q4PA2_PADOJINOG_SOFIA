#OOP
from pyscript import document, display


class Car: 
    def __init__(self, brand, model, type, color):
        self.brand = brand
        self.model = model
        self.type = type
        self.color = color

    def honk(self): 
        display(f'Beep Beep Beep', target = 'output')


# instantiating an object
car1 = Car('Fortuner', 'Model Y', 'Pink', 'EV') 
car1.honk()
car2 = Car('Tesla', 'Model X', 'Rainbow', 'VE') 

display(f'Mergal\'s car is a {car1.brand}. The color is car {car1.color}', target='output')
display(f'Macabago\'s car is a {car2.brand}. The color is car {car2.color}', target='output')

class Lexus(Car):
    pass

car1 = Lexus('Lexus', 'LM', 'Van', 'Gray')
car1.honk()

display(f'Law\'s car is a {car1.brand}. The color is {car1.color}', target='output')

# Parent Class
class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

# Child Class
class Puppy(Dog):
    pass

# 3 Dog Objects
dog1 = Dog("Luna", "German Shepherd", 1, "black")
dog2 = Dog("Jinro", "Shih Poo", 5, "brown")
dog3 = []

def create_dog(e):
    document.getElementById('output').innerHTML = ''
    name = document.getElementById("name").value
    breed = document.getElementById("breed").value
    age = int(document.getElementById("age").value)
    color = document.getElementById("color").value

    if name == "" or breed == "" or age == "" or color == "":
        display("⚠️ Please fill all information first.", target="output")
        return

    new_dog = Puppy(name, breed, age, color)
    dog3.append(new_dog)

    display(f"{dog1.name} is a {dog1.age}-year-old {dog1.breed} with {dog1.color} fur.", target="output")
    display(f"{dog2.name} is a {dog2.age}-year-old {dog2.breed} with {dog2.color} fur.", target="output")
    for dog in dog3:
        display(f"{dog.name} is a {dog.age}-year-old {dog.breed} with {dog.color} fur.", target="output")