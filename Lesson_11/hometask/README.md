Zoo Animals Python Challenge
Imagine you are designing a program to manage a zoo. The goal is to create a set of classes to represent different types of animals in the zoo.

Task List:
Create a base class called Animal with the following attributes:

name (string): The name of the animal.
age (integer): The age of the animal.
Create two subclasses: Mammal and Bird that inherit from the Animal class.

Add a method called make_sound to the Animal class. This method should print a generic sound that the animal makes.

Create two subclasses of Mammal: Lion and Elephant. Implement the make_sound method in each subclass to print a specific sound for that animal type.

Create two subclasses of Bird: Parrot and Eagle. Implement the make_sound method in each subclass to print a specific sound for that bird type.

Write a function called zoo_announcement that takes a list of animals and prints an announcement for each animal, including its name, age, and the sound it makes.

Create instances of each animal type and test your zoo_announcement function with these instances.

Example Usage:
# Your implementation here...

# Create instances of animals
lion = Lion("Simba", 5)
elephant = Elephant("Dumbo", 3)
parrot = Parrot("Polly", 2)
eagle = Eagle("Eddie", 4)

# Test the zoo_announcement function
animals_in_zoo = [lion, elephant, parrot, eagle]
zoo_announcement(animals_in_zoo)