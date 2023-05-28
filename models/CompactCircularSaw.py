"""
class file of a compact circular saw
"""
from models.Saw import Saw


class CompactCircularSaw(Saw):
    """
    Class representing a compact circular saw
    """

    def __init__(self, brand="CompCircSaw1", power=1200, runtime=6.0, blade_diameter=160, is_working=False):
        super().__init__(brand, power, runtime, is_working)
        self.blade_diameter = blade_diameter

    def get_remaining_work_time(self):
        """
        Method to get the remaining work time of the compact circular saw
        """
        return self.power / self.blade_diameter * self.runtime

    def __str__(self):
        return f"{self.brand} (power: {self.power}W, runtime: {self.runtime} hours, " \
               f"blade diameter: {self.blade_diameter}mm, is working: {self.is_working})"

    def start(self):
        """
        Method starts a compact circular saw
        """
        self.is_working = True

    def stop(self):
        """
        Method stops a compact circular saw
        """
        self.is_working = False
