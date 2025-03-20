class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic animal sound")


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Lion(Mammal):
    def make_sound(self):
        print("Roar")


class Elephant(Mammal):
    def make_sound(self):
        print("Trumpet")


class Parrot(Bird):
    def make_sound(self):
        print("Squawk")


class Eagle(Bird):
    def make_sound(self):
        print("Screech")


def zoo_announcement(animals):
    for animal in animals:
        print(f"{animal.name}, age {animal.age}, says: ")
        animal.make_sound()


# Create instances of animals
lion = Lion("Simba", 5)
elephant = Elephant("Dumbo", 3)
parrot = Parrot("Polly", 2)
eagle = Eagle("Eddie", 4)

# Test the zoo_announcement function
animals_in_zoo = [lion, elephant, parrot, eagle]
zoo_announcement(animals_in_zoo)