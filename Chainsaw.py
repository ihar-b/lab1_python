class Chainsaw:
    instance = None

    def __init__(self, brand="MS", power=1000, fuel_tank_capacity=5.0, fuel_level=3.0):
        self.brand = brand
        self.power = power
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_level = fuel_level
        self.is_working = False

    def start(self):
        self.is_working = True

    def stop(self):
        self.is_working = False

    def cut_wood(self, length):
        fuel_consumption = length / 10
        if fuel_consumption > self.fuel_level:
            self.is_working = False
            print("Not enough fuel to cut wood")
            return
        self.fuel_level -= fuel_consumption

    @staticmethod
    def get_instance():
        Chainsaw.instance = Chainsaw()
        return Chainsaw.instance

    def __str__(self):
        return f"{self.brand} (power: {self.power}W, fuel tank capacity: {self.fuel_tank_capacity}L," \
               f" fuel level: {self.fuel_level}L, is working: {self.is_working})"


chainsaw = Chainsaw("Makita", 2200, 3.5, 1.0)
print(chainsaw)

__chainsaw = Chainsaw()
print(__chainsaw)

chainsaw.start()
print(chainsaw)

chainsaw.cut_wood(2.5)
print(chainsaw)

chainsaw.cut_wood(1.5)
print(chainsaw)

chainsaw.stop()
print(chainsaw)

print(Chainsaw.get_instance())
