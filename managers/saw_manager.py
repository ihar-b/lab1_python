"""
class file to manage saws
"""
from models.chainsaw import Chainsaw
from models.electric_saw import ElectricSaw
from models.compact_circular_saw import CompactCircularSaw
from models.band_saw import BandSaw


class SawManager:
    """
    Class to manage saws
    """

    def __init__(self):
        self.saws = []

    def find_saws_with_more_power_than(self, power):
        """
        method to filter saws and to output ones with more power
        """
        saws_power_filtered = filter(lambda i: i.power > power, self.saws)
        return saws_power_filtered

    def find_saws_with_more_runtime_than(self, runtime):
        """
        method to filter saws and to output ones with more runtime
        """
        saws_runtime_filtered = list(filter(lambda i: i.runtime > runtime, self.saws))
        return saws_runtime_filtered

    def __len__(self):
        return len(self.saws)

    def __iter__(self):
        return iter(self.saws)

    def __getitem__(self, item):
        return self.saws[item]

    def get_power(self):
        return [x.power for x in self.saws]

    def enumerate(self):
        return [(index, obj) for index, obj in enumerate(self.saws)]

    def zip(self):
        return list(zip(self.saws, self.get_power()))

    def to_dict(self, data_type):
        return [{key: value for (key, value) in x.__dict__.items() if type(value) is data_type} for x in self.saws]

    def validation(self, validate):
        return {
            'all': all(map(validate, self.saws)),
            'any': any(map(validate, self.saws)),
        }

    def print_list(self):
        """
        method to output the list of saws
        """
        for saw1 in self.saws:
            print(saw1)

    def add_saw(self, saw1):
        """
        Method to add Saws
        """
        self.saws.append(saw1)


if __name__ == '__main__':
    saw_manager = SawManager()
    saw_manager.add_saw(Chainsaw("superCh", 1500, 10.0, 15, 5))
    saw_manager.add_saw(ElectricSaw("superElSaW", 500, 4.0, 1500))
    saw_manager.add_saw(BandSaw("superBandSaw", 800, 6.0, 1000))
    saw_manager.add_saw(CompactCircularSaw("superCompSaw", 1000, 5.0, 150))

    for saw in saw_manager.find_saws_with_more_runtime_than(5.0):
        print(saw)

    print("second filter:")

    for saw in saw_manager.find_saws_with_more_power_than(1000):
        print(saw)

    print(saw_manager.get_power())
    enumeration = saw_manager.enumerate()
    print(enumeration)
    print(saw_manager.zip())
    print(saw_manager.to_dict(int))
    print(saw_manager.validation(lambda x: x.power > 1000))
