class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 150
        self.energy = 150

    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping. Energy increased to {self.energy}.")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating. Energy increased to {self.energy}, health increased to {self.health}.")

    def play(self):
        self.health += 5
        print(f"{self.name} is playing. Health increased to {self.health}.")

    def noise(self):
        print(f"{self.name} makes a noise.")

class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Dog", tricks)

    def noise(self):
        print(f"{self.name} barks.")

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Cat", tricks)

    def noise(self):
        print(f"{self.name} meows.")
