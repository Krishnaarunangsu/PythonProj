class Engine:
    """
    Parent class
    """

    def __init__(self, power):
        """
        Constructor
        :param power:
        """
        self.power = None

    def set_power(self, power):
        self.power = power


class CombustionEngine(Engine):
    """
    Child class inherited from Engine
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


class ElectricEngine(Engine):
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


class HybridEngine(CombustionEngine, ElectricEngine):
    """
    Child class inherited from CombustionEngine and ElectricEngine
    """

    def __init__(self, is_engine_hybrid: bool):
        """
        Constructor
        """
        self.is_engine_hybrid = is_engine_hybrid

    def print_details(self):
        """
        Print the details of the car
        :return:
        """
        print("Power:", self.power)
        print("Tank Capacity:", self.tank_capacity)
        print("Charge Capacity:", self.charge_capacity)
        print(f'Is the engine hybrid?:{self.is_engine_hybrid}')


def main():
    """
    Coordinate all the activities
    :return:
    """
    car = HybridEngine(True)
    car.set_power("2000 CC")
    car.set_charge_capacity("250 W")
    car.set_tank_capacity("20 Litres")
    car.print_details()


if __name__ == "__main__":
    main()
