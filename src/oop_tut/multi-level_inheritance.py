class Vehicle:
    """
    parent class
    """

    def __init__(self, speed):
        """
        Constructor
        """
        self.top_speed = speed

    def set_top_speed(self):
        """
        defining the set top speed
        :param speed:
        :return:
        """
        print(f"Top speed is set to:{self.top_speed}")


class Car(Vehicle):
    """
    child class of Vehicle
    """

    def __init__(self, car_type):
        """
        Constructor
        """
        Vehicle.__init__(self, 200)
        self.car_type = car_type

    def open_trunk(self):
        print("Trunk is now open.")
        print(f'The Car Type is:{self.car_type}')


class Hybrid(Car):
    """
    Hybrid: Instance of Car
    """

    def __init__(self, is_hybrid: bool):
        """
        Constructor
        """
        Car.__init__(self, 'Corolla')
        self.is_hybrid = is_hybrid

    def turn_on_hybrid(self):
        """
        Is Hybrid turned On?
        :return:
        """
        print(f"Hybrid::{self.is_hybrid}")


def main():
    """
    Coordinate all the activities
    :return:
    """
    vehicle = Vehicle(200)
    car = Car('Corolla')
    prius_prime = Hybrid(True)  # creating an object of the Hybrid class
    prius_prime.set_top_speed()  # accessing methods from the parent class
    prius_prime.open_trunk()  # accessing method from the parent class
    prius_prime.turn_on_hybrid()  # accessing method from the child class


if __name__ == "__main__":
    main()
