class Vehicle:

    def __init__(self, brand: str, max_speed: float):
        self.brand = brand
        self.max_speed = max_speed

    def print_info(self):
        print(f"I'm vehicle: {self.brand} - {self.max_speed}")


class Car(Vehicle):

    def __init__(self, brand: str, max_speed: float, color: str = "white"):
        super().__init__(brand, max_speed)
        self.color = color


    def print_info(self):
        print(f"I'm {self.color} car: {self.brand} - {self.max_speed}")


vehicle = Vehicle("general", 300)
vehicle.print_info()

car = Car("bmw", 450, "black")
car.print_info()