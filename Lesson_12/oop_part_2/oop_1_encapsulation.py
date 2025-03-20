class Vehicle:

    def __init__(self, brand: str, max_speed: float):
        self.__max_speed = max_speed if max_speed > 90 else 90  # -> private
        self._brand = brand  # -> protected

    def print_info(self):
        print(f"I'm vehicle: {self._brand} - {self.__max_speed}")

    def get_max_speed(self):
        return self.__max_speed

    @property
    def brand(self):
        return self._brand

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed if max_speed > 90 else 90

    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand



vehicle = Vehicle("general", 100)

# protected member usage out of the class

# vehicle._brand = "new brand"
# print(vehicle._brand)

# private member usage out of the class

# print(vehicle.__max_speed) # AttributeError: 'Vehicle' object has no attribute '__max_speed'
print(f"{vehicle._Vehicle__max_speed = }") # name mangling
print(vehicle.get_max_speed())
vehicle.set_max_speed(150)
print(vehicle.get_max_speed())
vehicle.set_max_speed(-95)
print(vehicle.get_max_speed())

vehicle.brand = "BMW"
print(vehicle.brand)