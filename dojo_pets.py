# initialize Ninja class
class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(name='', type='', tricks='', health = 0, energy = 0)

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

# initialize Pet class 
class Pet:

    def __init__(self, name, type, tricks, health = 0, energy = 0):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25

    def play(self):
        self.health += 5

    def eat(self):
        self.energy += 5
        self.health += 10

    def noise(self):
        print('yass queen')


ninja_1 = Ninja("Jacob", "Sexton", "Catnip", "Tuna", "Cat")
pet_1 = Pet("Ghost", "Cat", "Backflip")

print(ninja_1.treats)
print(pet_1.tricks)
ninja_1.walk()
print(pet_1.health)
ninja_1.feed()
print(pet_1.health)
print(pet_1.energy)
ninja_1.bathe()
