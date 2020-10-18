class Squeezer:
    number_of_comparisons = 0
    number_of_swaps = 0

    def __init__(self, color=None, power_consumption_in_kilowatts=0, productivity_in_litres_per_hour=0):
        self.color = color
        self.power_consumption_in_kilowatts = power_consumption_in_kilowatts
        self.productivity_in_litres_per_hour = productivity_in_litres_per_hour

    def __repr__(self):
        return f"color: {self.color}, power: {self.power_consumption_in_kilowatts}, " \
               f"prod: {self.productivity_in_litres_per_hour}"
