"""
class file band saw
"""
from models.saw import Saw


class BandSaw(Saw):
    """
    Class representing a band saw
    """

    def __init__(self, brand="bandsaw1", power=2000, runtime=10.0, blade_length=1500, is_working=False):
        super().__init__(brand, power, runtime, is_working)
        self.blade_length = blade_length

    def get_remaining_work_time(self):
        """
        Method to get the remaining work time of the band saw
        """
        return 0

    def __str__(self):
        return f"{self.brand} (power: {self.power}W, runtime: {self.runtime} hours, " \
               f"blade length: {self.blade_length}mm, is working: {self.is_working})"

    def start(self):
        """
        Method starts a band saw
        """
        self.is_working = True

    def stop(self):
        """
        Method stops a band saw
        """
        self.is_working = False
