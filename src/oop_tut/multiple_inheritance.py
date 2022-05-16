class CombustionEngine:
    """

    """

    def __init__(self):
        """
        Constructor
        """
        self.tank_capacity = None

    def set_tank_capacity(self, tank_capacity):
        """
        Set the tank capacity
        :param tank_capacity:
        :return:
        """
        self.tank_capacity = tank_capacity


class ElectricEngine():
    """
    Child class inherited from Engine
    """

    def __init__(self):
        """
        Constructor
        """
        self.charge_capacity = None

    def set_charge_capacity(self, charge_capacity):
        """
        Set the Charge capacity
        :param charge_capacity:
        :return:
        """
        self.charge_capacity = charge_capacity


# Child class inherited from CombustionEngine and ElectricEngine
class HybridEngine(CombustionEngine, ElectricEngine):
    """

    """

    def __init__(self):
        """
        Constructor
        """

    def print_details(self):
        """

        :return:
        """
        print("Tank Capacity:", self.tank_capacity)
        print("Charge Capacity:", self.charge_capacity)


def main():
    """
    Coordinate all the activities
    :return:
    """
    car = HybridEngine()
    car.set_charge_capacity("250 W")
    car.set_tank_capacity("20 Litres")
    car.print_details()


if __name__ == "__main__":
    main()
