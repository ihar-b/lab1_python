"""
file of an abstract class
"""
from abc import ABC, abstractmethod


class Saw(ABC):
    """
    Abstract class representing a saw
    """

    def __init__(self, brand, power, runtime, is_working=False):
        self.brand = brand
        self.power = power
        self.runtime = runtime
        self.is_working = is_working

    @abstractmethod
    def get_remaining_work_time(self):
        """
        Abstract method to get the remaining work time of the saw
        """

    def __getitem__(self, item):
        return type(item), item

    def __str__(self):
        return f"{self.brand} (power: {self.power}W, runtime: {self.runtime} hours, is working: {self.is_working})"
