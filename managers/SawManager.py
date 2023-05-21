"""
class file to manage saws
"""
from models.Chainsaw import Chainsaw
from models.ElectricSaw import ElectricSaw
from models.CompactCircularSaw import CompactCircularSaw
from models.BandSaw import BandSaw


class SawManager:
    """
    Class to manage saws
    """


if __name__ == "__main__":
    ch1 = Chainsaw()
    el1 = ElectricSaw()
    band1 = BandSaw()
    comp1 = CompactCircularSaw()
    ch = Chainsaw("superCh", 1500, 10.0, 15, 5)
    el = ElectricSaw("superElSaW", 500, 4.0, 1500)
    band = BandSaw("superBandSaw", 800, 6.0, 1000)
    comp = CompactCircularSaw("superCompSaw", 1000, 5.0, 150)
    saws = [ch, el, band, comp, ch1, el1, band1, comp1]


    def print_list():
        """
        method to output the list of saws
        """
        for saw1 in saws:
            print(saw1)


    def add_saw(saw2):
        """
        Method to add Saws
        """
        saws.append(saw2)


    def find_saws_with_more_power_than(power):
        """
        method to filter saws and to output ones with more power
        """
        saws_power_filtered = list(filter(lambda i: i.power > power, saws))
        return saws_power_filtered


    def find_saws_with_more_runtime_than(runtime):
        """
        method to filter saws and to output ones with more runtime
        """
        saws_runtime_filtered = list(filter(lambda i: i.runtime > runtime, saws))
        return saws_runtime_filtered


    for saw in find_saws_with_more_runtime_than(5.0):
        print(saw)

    print("second filter:")

    for saw in find_saws_with_more_power_than(1000):
        print(saw)
