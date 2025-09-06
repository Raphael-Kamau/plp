
# Activity 1 
# 1. Create a class representing anything you like 
# 2. Add attributes and methods to bring the class to life!
# 3. Use constructors to initialize each object with unique values
class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.color = color

    def make_call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def send_message(self, number, message):
        return f"Sending message to {number}: {message}"

    def get_specs(self):
        return f"{self.brand} {self.model} - {self.storage}GB - {self.color}"

# Subclass representing a specific type of smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, color, gpu):
        super().__init__(brand, model, storage, color)
        self.gpu = gpu  # Additional attribute for gaming phones

    def play_game(self, game_name):
        return f"Playing {game_name} on {self.brand} {self.model} with {self.gpu} GPU."



# Activity 2
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses with their own move() implementations, each overrides the move() method with unique behavior
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Function to demonstrate polymorphism
# this action accepts any Vehicle object and calls its move() method, which shows polymorphic behavior
def travel(vehicle: Vehicle):
    vehicle.move()

# Create instances
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Test polymorphic behavior
for v in vehicles:
    travel(v)
