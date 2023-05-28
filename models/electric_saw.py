"""
Class file of the electric saw
"""
from models.saw import Saw


class ElectricSaw(Saw):
    """
    Class representing an electric saw
    """

    def __init__(self, brand="elsaw1", power=1500, runtime=8.0, battery_capacity=6000, is_working=False):
        super().__init__(brand, power, runtime, is_working)
        self.battery_capacity = battery_capacity

    def get_remaining_work_time(self):
        """
        Method to get the remaining work time of the electric saw
        """
        return self.power / self.battery_capacity * self.runtime

    def __str__(self):
        return f"{self.brand} (power: {self.power}W,runtime: {self.runtime} hours, " \
               f" battery capacity: {self.battery_capacity}mAh, is working: {self.is_working})"

    def start(self):
        """
        method starts an electric saw
        """
        self.is_working = True

    def stop(self):
        """
        method stops an electric saw
        """
        self.is_working = False
