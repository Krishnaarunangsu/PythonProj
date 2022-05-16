class Vehicle:
    """
    parent class
    """

    def __init__(self):
        """
        Constructor
        """
        self.top_speed = None

    def set_top_speed(self, top_speed):  # defining the set
        self.top_speed = top_speed
        print("Top speed is set to", self.top_speed)


class Car(Vehicle):
    """
    child class of Vehicle
    """

    def __init__(self):
        """
        Constructor
        """
        self.is_trunk_open = False

    def open_trunk(self, is_trunk_open):
        """
        Is Trunk Open
        :param is_trunk_open:
        :return:
        """
        self.is_trunk_open = is_trunk_open
        print(f"Trunk is now open:{self.is_trunk_open}")


class Hybrid(Car):
    """
    Hybrid car child class of Car
    """

    def __init__(self):
        """
        Constructor
        """
        self.is_hybrid = False

    def turn_on_hybrid(self, is_hybrid):
        """
        Is The Car Hybrid
        :param is_hybrid:
        :return:
        """
        self.is_hybrid = is_hybrid
        print(f"Hybrid mode is now switched on:{self.is_hybrid}")


def main():
    """
    Coordinate all the activities
    :return:
    """
    prius_prime = Hybrid()  # creating an object of the Hybrid class
    prius_prime.set_top_speed(220)  # accessing methods from the parent class
    prius_prime.open_trunk(False)  # accessing method from the parent class
    prius_prime.turn_on_hybrid(True)  # accessing method from the child class


if __name__ == "__main__":
    main()
