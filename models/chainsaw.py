"""
file of chainsaw class
"""
from models.saw import Saw
from decorators.logging_1 import logged
from exeptions.exeption_1 import CustomException


class Chainsaw(Saw):
    """
    Class file of a chainsaw
    """

    def __init__(self, brand="MS", power=1000, runtime=5.0, max_fuel_level=10, curr_fuel_level=5, is_working=False):
        super().__init__(brand, power, runtime, is_working)
        self.max_fuel_level = max_fuel_level
        self.curr_fuel_level = curr_fuel_level

    def start(self):
        """
        Method to start the chainsaw
        """
        self.is_working = True

    def stop(self):
        """
        Method to stop the chainsaw
        """
        self.is_working = False

    @logged(CustomException, "console")
    def cut_wood(self, length):
        """
        Method to calculate the length of cut wood
        """
        if not self.is_working:
            raise CustomException("Chainsaw is not working. Start the chainsaw first.")

        fuel_consumption = length / 10
        if fuel_consumption > self.runtime:
            self.is_working = False
            print("Not enough engine runtime to cut wood")
            return

        self.runtime -= fuel_consumption

    def get_remaining_work_time(self):
        """
        Method to get the remaining work time of the chainsaw
        """
        return self.curr_fuel_level / self.max_fuel_level * self.runtime

    def __str__(self):
        return f"{self.brand} (power: {self.power}W, max fuel level: {self.max_fuel_level}L," \
               f" fuel level: {self.curr_fuel_level}L, is working: {self.is_working})"
