class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet=None):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(self.first_name + " walks " +  self.pet.name +"!  They had a great time!")
        return self

    def feed(self):
        self.pet.eat()
        print(self.first_name + " fed " + self.pet.name + " some kibble! ")
        return self

    def bathe(self):
        self.pet.noise()
        print(self.pet.name + " took a bath!")
        return self

class Pet:
    def __init__(self, name, type, tricks, health=50, energy=50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print(self.name + " takes a nap!  Their energy increase by 25!")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.name + " ate some food!  Their energy increased by 5 and its health increased by 10!")
        return self

    def play(self):
        self.health += 5
        print(self.name + " played with you!  Their health increase by 5!")
        return self

    def noise(self):
        print(self.name + " barks at you!  Woof woof!")
        return self

pet = Pet('Ivy', 'Goldendoodle', 'sit')
ninja_Jacob = Ninja('Jacob', 'Pavelka', 'MilkBones', 'Purina', pet)

ninja_Jacob.walk().bathe()